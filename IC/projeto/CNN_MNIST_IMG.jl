using LinearAlgebra, Statistics, Flux, MLDatasets, Plots, CUDA
using BetaML: ConfusionMatrix, fit!, info
using Printf
using BSON
using Images, Random
using Base.Filesystem

DEBUG = true
NCLASSES = 0
USING_MODEL = "cnn_mnist_img.bson"

dir_imgs_prep_train = "pre-proc/seg_train/"
dir_imgs_prep_test = "pre-proc/seg_test/"

###### Funções auxiliares para coleta de dados ######

# Carrega imagens e associa a sua label de classe
function carrega_imgs(diretorio::String, classe_label::Int64)
        
    nome_imgs = readdir(diretorio)
    
    imgs = []
    for nome_img in nome_imgs

        # carrega imagem
        img = load(string(diretorio, nome_img))
        # separa canais
        img = channelview(img)
        # adiciona em um array juntamente com sua label
        push!(imgs, (img, classe_label))

    end

    return imgs
end

# Retorna a quantidade de classes abordadas no modelo
function retorna_n_classes()

    classes = readdir(dir_imgs_prep_train)
    quantidade_classes = NCLASSES === 0 ? size(classes,1) : min(NCLASSES, size(classes,1))

    return quantidade_classes

end

# Retorna uma permutação dotreino e teste
function retorna_teste_treino(srand_personalizado::Int64=0)

    classes = readdir(dir_imgs_prep_train)
    quantidade_classes = retorna_n_classes()

    # carrega imagens em um vetor [] -> (img, classe_int), um para treino outro para testes
    vetor_treinos = nothing
    vetor_testes = nothing
    for pos_c in eachindex(classes)
        if pos_c > quantidade_classes
            break
        end
        treino = carrega_imgs(string(dir_imgs_prep_train, classes[pos_c], "/"), pos_c-1)
        teste = carrega_imgs(string(dir_imgs_prep_test, classes[pos_c], "/"), pos_c-1)
        vetor_treinos = vetor_treinos === nothing ? treino : vcat(vetor_treinos, treino)
        vetor_testes = vetor_testes === nothing ? teste : vcat(vetor_testes, teste)
    end

    # Seed personalizada
    if srand_personalizado !== 0
        srand(srand_personalizado)
    end

    # Define uma permutação de treinos diferente a cada execução
    vetor_treinos_permutado = nothing
    size_v = size(vetor_treinos,1)

    for _ in 1:size_v
        # Escolhe um inteiro aleatorio [1, size(vetor_treinos)]
        rnd = max(round(Int, rand(Float64)*size(vetor_treinos,1)), 1)
        # Adiciona a permutacao
        vetor_treinos_permutado = vetor_treinos_permutado === nothing ? 
            vetor_treinos[rnd] : vcat(vetor_treinos_permutado, vetor_treinos[rnd])
        # remove do vetor original
        deleteat!(vetor_treinos, rnd)
    end

    x_treino = nothing
    x_teste = nothing
    y_treino = []
    y_teste = []

    # formata a saida de treino
    for pos_v in 1:size_v
        x_treino = x_treino === nothing ? 
            reshape(vetor_treinos_permutado[pos_v][1], (1,3,28,28)) :
            vcat(x_treino, reshape(vetor_treinos_permutado[pos_v][1], (1,3,28,28)))
        push!(y_treino, vetor_treinos_permutado[pos_v][2])
    end

    # formata a saida de teste
    size_v = size(vetor_testes, 1)
    for pos_v in 1:size_v
        x_teste = x_teste === nothing ? 
            reshape(vetor_testes[pos_v][1], (1,3,28,28)) :
            vcat(x_teste, reshape(vetor_testes[pos_v][1], (1,3,28,28)))
        push!(y_teste, vetor_testes[pos_v][2])
    end

    return x_treino, y_treino, x_teste, y_teste, quantidade_classes
end

###### ######

###### Fluxo de testes do modelo ######

function testar_modelo()

    # Carrega labels e o modelo
    classes = readdir(dir_imgs_prep_train)
    BSON.@load USING_MODEL modelo

    while true

        println("Escreva o nome de uma instancia de testes no formato classe/nome_da_imagem:")
        str = readline()
        
        if !occursin("/", str)
            @warn("String nao contem /!")
            continue
        end

        strsplit = split(str, "/")
        classe = strsplit[1]

        if ! (classe in classes)
            @warn("Classe não existe!")
            continue
        end
        
        if !isfile(string(dir_imgs_prep_test, str))
            @warn("Imagem não existe!")
            continue
        end

        # configura a imagem para classificar como e configurado no modelo
        img = load(string(dir_imgs_prep_test, str))
        img = channelview(img)
        img = reshape(img, (1,3,28,28))
        img = permutedims(img, (4,3,2,1))
        img = convert(Array{Float32,4}, img)
        img = reshape(img, (28,28,3,1))
        média_img = mean(img)
        desvio_img = std(img)
        img = (img .- média_img) ./ desvio_img

        # retorna a classificação atribuida a imagem
        resul = Flux.onecold(modelo(img), classes[1:retorna_n_classes()])
        @info(string("O modelo classificou em: ", resul))
    end
end

###### Fluxo de treino do modelo ######

function treinar_modelo()

    @info("Iniciando a CNN ...")
    x_treino, y_treino, x_teste, y_teste, n_classes = retorna_teste_treino()
    @info("Dados de teste e treino recebidos")

    # Ajustando parametros de treino
    x_treino = permutedims(x_treino, (4,3,2,1))
    x_treino = convert(Array{Float32,4}, x_treino)
    x_treino = reshape(x_treino, (28,28,3,size(x_treino,4)))
    média_x_treino = mean(x_treino)
    desvio_x_treino = std(x_treino)
    x_treino = (x_treino .- média_x_treino) ./ desvio_x_treino

    # Ajustando parametros de teste
    x_teste = permutedims(x_teste, (4,3,2,1))
    x_teste = convert(Array{Float32,4}, x_teste)
    x_teste = reshape(x_teste, (28,28,3,size(x_teste,4)))
    média_x_teste = mean(x_teste)
    desvio_x_teste = std(x_teste)
    x_teste = (x_teste .- média_x_teste) ./ desvio_x_teste

    @info("Parametros ajustados")

    # salva imagens que serao utilizadas no modelo para verificação de corretude
    if DEBUG

        @debug("Salvando imagens a serem recebidas pela CNN")

        classes = readdir(dir_imgs_prep_train)

        if !isdir("debugImgs/")
            mkdir("debugImgs/")
            mkdir("debugImgs/Test")
            mkdir("debugImgs/Training")
            for class in classes
                mkdir(string("debugImgs/Test/", class))
                mkdir(string("debugImgs/Training/", class))
            end
        end

        # treino
        imgsRGBTreino = permutedims(x_treino, (3,2,1,4))
        for pos in 1:size(x_treino, 4)
            save(string("debugImgs/Training/",classes[y_treino[pos]+1], "/", pos, ".jpg"), colorview(RGB, imgsRGBTreino[:,:,:,pos]))
        end

        # testes
        imgsRGBTeste = permutedims(x_teste, (3,2,1,4))
        for pos in 1:size(x_teste, 4)
            save(string("debugImgs/Test/", classes[y_teste[pos]+1], "/", pos, ".jpg"), colorview(RGB, imgsRGBTeste[:,:,:,pos]))
        end

        @debug("Imagens salvas")
        
    end

    y_treino = Flux.onehotbatch(y_treino, 0:n_classes-1)
    y_teste = Flux.onehotbatch(y_teste, 0:n_classes-1)
    dados_treino = Flux.Data.DataLoader((x_treino, y_treino), batchsize=32)

    # Tamanho resultante = ((W – F + 2P) / S) + 1, onde:
    #     W de WxW é o tamanho da imagem original
    #     F de FxF é o tamanho do filtro
    #     P é o padding
    #     S é o stride
    modelo = Chain(
        # 28x28 => 28x28
        Conv((5, 5), 3=>32, pad=2, stride=1, relu),
        # 28x28 => 24x24
        Conv((5, 5), 32=>32, stride=1, relu, bias=false),
        # 24x24 => 24x24
        BatchNorm(32, relu),
        # 24x24 => 12x12
        MaxPool((2,2)),
        # 12x12 => 12x12
        Dropout(0.1),
        # 12x12 => 10x10
        Conv((3, 3), 32=>64, stride=1, relu),
        # 10x10 => 8x8
        Conv((3, 3), 64=>64, stride=1, relu, bias=false),
        # 8x8 => 8x8
        BatchNorm(64, relu),
        # 8x8 => 4x4
        MaxPool((2,2)),
        # 4x4 => 4x4
        Dropout(0.1),
        # 64x4x4 => 1064
        Flux.flatten,
        # 1024 => 256
        Dense(1024, 256, bias=false),
        # 256 => 256
        BatchNorm(256, relu),
        # 256 => 128
        Dense(256, 128, bias=false),
        # 128 => 128
        BatchNorm(128, relu),
        # 128 => 84
        Dense(128, 84, bias=false),
        # 84 => 84
        BatchNorm(84, relu),
        # 84 => 84
        Dropout(0.1),
        # 84 => n_classes()
        Dense(84, retorna_n_classes()),
        # Classificador probabilistico na saída
        Flux.softmax
    )

    acuracia(ŷ, y) = (mean(Flux.onecold(ŷ) .== Flux.onecold(y)))
    perda(x, y) = Flux.crossentropy(modelo(x), y)

    opt = Flux.ADAM(3e-5)  # taxa de aprendizagem
    ps  = Flux.params(modelo)

    num_épocas = 6
    melhor_acu = 0.0
    última_melhoria = 0
    ŷteste = nothing

    @info("Modelo construído, iniciando treinamento")

    for época in 1:num_épocas
    
        @info(string("Época ", época))
        Flux.train!(perda, ps, dados_treino, opt)
    
        # Calcule a acurácia:
        ŷteste = modelo(x_teste)
        acu = acuracia(ŷteste, y_teste)
    
        @info(@sprintf("[%d]: Acurácia nos testes: %.4f", época, acu))
    
        # Se a acurácia for muito boa, termine o treino
        if acu >= 0.999
            @info(" -> Término prematuro: alcançamos uma acurácia de 99.9%")
            BSON.@save USING_MODEL modelo
            break
        end
        
        # Se isto é a melhor acurácia vista até agora, salve o modelo
        if acu >= melhor_acu
            @info(" -> Uma nova melhor acurácia! Salvando o modelo para mnist_conv.bson")
            BSON.@save USING_MODEL modelo
            melhor_acu = acu
            última_melhoria = época
        end
        
        # Se não houve melhoria em 5 épocas, reduza a taxa de aprendizagem:
        if época - última_melhoria >= 5 && opt.eta > 1e-6
            opt.eta /= 10.0
            @warn(" -> Sem melhoria por enquanto, reduzindo a taxa de aprendizagem para $(opt.eta)!")
            
            # Após reduzir a taxa de aprendizagem, dê a ela umas poucas épocas para melhorar
            última_melhoria = época
        end
        
        if época - última_melhoria >= 10
            @warn(" -> Consideramos que houve convergência.")
            break
        end
    end

    ŷtreino = modelo(x_treino)
    ŷteste = modelo(x_teste)

    acuracia(ŷtreino, y_treino)
    acuracia(ŷteste, y_teste)

    cm = ConfusionMatrix()
    fit!(cm, Flux.onecold(y_teste) .-1, Flux.onecold(ŷteste) .-1)
    print(cm)

    res = info(cm)

    heatmap(
        string.(res["categories"]),
        string.(res["categories"]),
        res["normalised_scores"],
        seriescolor=cgrad([:white,:blue]),
        xlabel="Predito",
        ylabel="Real",
        title="Matriz de Confusão (scores normalizados)"
    )

    # Limita o mapa de cores, para vermos melhor onde os erros estão

    heatmap(
        string.(res["categories"]),
        string.(res["categories"]),
        res["normalised_scores"],
        seriescolor=cgrad([:white,:blue]),
        clim=(0., 0.02),
        xlabel="Predito",
        ylabel="Real",
        title="Matriz de Confusão (scores normalizados)"
    )
end

###### ######

function main()

    println("Bem vindo, digite 1 para testar a CNN ou 2 para treinar:")
    
    num = 0
    while true

        num = readline()
        if tryparse(Int64, num) !== nothing
            num = parse(Int64, num)
            if num == 1 || num == 2
                break
            end
        end
        @warn("Valor inválido!")
    end

    if num == 1
        testar_modelo()
    else
        treinar_modelo()
    end
end

main()