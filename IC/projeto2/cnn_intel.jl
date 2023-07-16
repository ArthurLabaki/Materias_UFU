#Imports

using LinearAlgebra, Statistics, Flux, MLDatasets, Plots, CUDA
using BetaML: ConfusionMatrix, fit!, info
using Printf, BSON
using Images, Base.Filesystem

NCLASSES = 0
USING_MODEL = "CNN_INTEL_NOVO2.bson"

# getting our dataset
dir_imgs_pre_process_train = "pre_process/seg_train/"
dir_imgs_pre_process_test = "pre_process/seg_test/"

function return_classes_quantity()
    classes = readdir(dir_imgs_pre_process_train)
    class_quantity = NCLASSES === 0 ? size(classes,1) : min(NCLASSES, size(classes,1))
    
    return class_quantity
end

function load_img(dir::String, class_index::Int64)
    img_names = readdir(dir)
    imgs = []
    for img_name in img_names
        img = load(string(dir, img_name))
        img = channelview(img)
        push!(imgs, (img, class_index))
    end
    return imgs
end 

function permutate_dataset(array_train::Array{Any}, srand_personalizado::Int64)
    if srand_personalizado !== 0
        srand(srand_personalizado)
    end

    array_train_perm = []
    array_size = size(array_train, 1)

    for _ in 1:array_size
        rnd = max(round(Int, rand(Float64)*size(array_train, 1)), 1)
        array_train_perm = vcat(array_train_perm, array_train[rnd])
        deleteat!(array_train, rnd)
    end

    return array_train_perm
end

function return_dataset(srand_personalizado::Int64=0)
    classes = readdir(dir_imgs_pre_process_train)
    quantidade_classes = return_classes_quantity()
    println(string("Quantidade de classes: ", quantidade_classes ))
    println("Classes: $classes")

    # carrega imagens em um vetor [] -> (img, classe_int), um para treino outro para testes
    vetor_treinos = nothing
    vetor_testes = nothing
    for pos_c in eachindex(classes)
        if pos_c > quantidade_classes
            break
        end
        treino = load_img(string(dir_imgs_pre_process_train, classes[pos_c], "/"), pos_c-1)
        teste = load_img(string(dir_imgs_pre_process_test, classes[pos_c], "/"), pos_c-1)
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

    println(string("Quantidade de imagens treino: ", size(vetor_treinos_permutado,1) ))
    println(string("Quantidade de imagens teste: ", size(vetor_testes,1) ))
    return x_treino, y_treino, x_teste, y_teste, quantidade_classes
end
    

function train_model()
    println("Obtendo dados")
    x_train, y_train, x_test, y_test, n_classes = return_dataset()
    println("Dados obtidos")

    # Ajustando parametros de treino
    x_train = permutedims(x_train, (4,3,2,1))
    x_train = convert(Array{Float32,4}, x_train)
    x_train = reshape(x_train, (28,28,3,size(x_train,4)))
    média_x_train = mean(x_train)
    desvio_x_train = std(x_train)
    x_train = (x_train .- média_x_train) ./ desvio_x_train

    # Ajustando parametros de teste
    x_test = permutedims(x_test, (4,3,2,1))
    x_test = convert(Array{Float32,4}, x_test)
    x_test = reshape(x_test, (28,28,3,size(x_test,4)))
    média_x_test = mean(x_test)
    desvio_x_test = std(x_test)
    x_test = (x_test .- média_x_test) ./ desvio_x_test

    println("Parametros ajustados")
    y_train = Flux.onehotbatch(y_train, 0:n_classes-1)
    y_test = Flux.onehotbatch(y_test, 0:n_classes-1)
    dados_treino = Flux.Data.DataLoader((x_train, y_train), batchsize=32)


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
          # 12x12 => 10x10
        Conv((3, 3), 64=>256, stride=1, relu),
        # 10x10 => 8x8
        Conv((3, 3), 256=>256, stride=1, relu, bias=false),
        # 8x8 => 8x8
        BatchNorm(256, relu),
        # 8x8 => 4x4
        MaxPool((2,2)),
        # 4x4 => 4x4
        Dropout(0.3),
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
        Dense(84, return_classes_quantity()),
        # Classificador probabilistico na saída
        Flux.softmax
    )

    




    acuracia(ŷ, y) = (mean(Flux.onecold(ŷ) .== Flux.onecold(y)))
    perda(x, y) = Flux.crossentropy(modelo(x), y)

    opt = Flux.ADAM(3e-5)  # taxa de aprendizagem
    ps  = Flux.params(modelo) #Parâmetros

    num_épocas = 11
    melhor_acu = 0.0
    última_melhoria = 0
    ŷtest = nothing

    println("Modelo da CNN construido")

    for época in 1:num_épocas
        @info(string("Época ", época))
        Flux.train!(perda, ps, dados_treino, opt)

        ŷtest = modelo(x_test)
        acu = acuracia(ŷtest, y_test)

        @info(@sprintf("[%d]: Acurácia nos testes: %.4f", época, acu))

        # Se a acurácia for muito boa, termine o treino
        if acu >= 0.999
            @info(" -> Término prematuro: alcançamos uma acurácia de 99.9%")
            BSON.@save USING_MODEL modelo
            break
        end
        
        # Se isto é a melhor acurácia vista até agora, salve o modelo
        if acu >= melhor_acu
            @info(" -> Uma nova melhor acurácia! Salvando o modelo")
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

    ŷtrain = modelo(x_train)
    ŷtest = modelo(x_test)

    acuracia(ŷtrain, y_train)
    acuracia(ŷtest, y_test)

    cm = ConfusionMatrix()
    fit!(cm, Flux.onecold(y_test) .-1, Flux.onecold(ŷtest) .-1)
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


function test_model()
    classes = readdir(dir_imgs_pre_process_train)
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
        
        if !isfile(string(dir_imgs_pre_process_test, str))
            @warn("Imagem não existe!")
            continue
        end

        # configura a imagem para classificar como e configurado no modelo
        img = load(string(dir_imgs_pre_process_test, str))
        img = channelview(img)
        img = reshape(img, (1,3,28,28))
        img = permutedims(img, (4,3,2,1))
        img = convert(Array{Float32,4}, img)
        img = reshape(img, (28,28,3,1))
        média_img = mean(img)
        desvio_img = std(img)
        img = (img .- média_img) ./ desvio_img

        # retorna a classificação atribuida a imagem
        resul = Flux.onecold(modelo(img), classes[1:return_classes_quantity()])
        @info(string("O modelo classificou em: ", resul))
    end
end

function main()
    println("Trabalho de Arthur e Vinnicius")
    println("Selecione 1 para treinar a rede | Selecione 2 para testar rede treinada")
    opt_selected = readline()
    if opt_selected == "1"
        println("Iniciando treinamento:")
        train_model()
    elseif opt_selected == "2"
        println("Iniciando testes:")
        test_model()
    else 
        @warn("Opção inválida")
    end
    
    
end

main()