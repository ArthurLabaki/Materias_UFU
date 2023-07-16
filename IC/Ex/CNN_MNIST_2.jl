using LinearAlgebra, Statistics, Flux, MLDatasets, Plots, CUDA
using BetaML: ConfusionMatrix, fit!, info
using Printf, BSON

# Recebe as imagems e converte o formato da matriz
x_treino, y_treino = MLDatasets.MNIST(split=:train)[:]
x_treino = permutedims(x_treino,(2,1,3)); # For correct img axis
x_treino = convert(Array{Float32,3},x_treino);
# Para funcionar no formato Flux, Dataloader itera na utima camada (60000) pegando matrizes 3D 28x28x1
x_treino = reshape(x_treino,(28,28,1,60000));
# Há a necessidade de padronizar para evitar a natureza errática da entrada
média_x_treino = mean(x_treino);
desvio_x_treino = std(x_treino);
# faz operações de normalização elemento a elemento na matriz 4D
x_treino = (x_treino .- média_x_treino) ./ desvio_x_treino;

# Cria o vetor one hot de labels para cada y_treino, usado pela CNN
y_treino = Flux.onehotbatch(y_treino, 0:9);
# Objeto que determina a organização do treino sobre os dados de entrada

x_teste, y_teste = MLDatasets.MNIST(split=:test)[:]
x_teste = permutedims(x_teste,(2,1,3)); # For correct img axis
x_teste = convert(Array{Float32,3},x_teste);
x_teste = reshape(x_teste,(28,28,1,10000));
média_x_teste = mean(x_teste);
desvio_x_teste = std(x_teste);
x_teste = ((x_teste .- média_x_teste) ./ desvio_x_teste)
y_teste = Flux.onehotbatch(y_teste, 0:9)

# converte para matrizes 784*60000
#x_treino = Flux.flatten(x_treino)
#y_treino = Flux.flatten(y_treino)
dados_treino = Flux.Data.DataLoader((x_treino, y_treino), batchsize=128)

#x_teste = Flux.flatten(x_treino)
#y_teste = Flux.flatten(y_treino)

# pad adicao de pixeis na borda
# stride indica o movimento da convolucao
# Tamanho resultante = (W – F + 2P) / S + 1, onde:
#     W de WxW é o tamanho da imagem original
#     F de FxF é o tamanho do filtro
#     P é o padding
#     S é o stride associado
#     Ex: Conv((5, 5), 1=>32,   pad=2, stride=1, ...) -> 
modelo = Chain(
   # Camada 1: 28x28 => 28x28
   Conv((5, 5), 1=>32, pad=2, stride=1, relu),
   # Camada 2: 28x28 => 24x24 -> meio que junta as 3 camadas 
   Conv((5, 5), 32=>32, stride=1, relu, bias=false),
   # Camada 3: 24x24 => 24x24 -> é uma função aplicada nos nós da rede neural
   BatchNorm(32, relu),
   # 24x24 => 12x12 -> filtro 2x2 coloca os maiores pela divisão do escopo da convolução geral 
   MaxPool((2,2)),
   # 12x12 => 12x12 -> Aleatoriamente desativa alguns, os nós só repassam
   Dropout(0.25),
   # 12x12 => 10x10
   Conv((3, 3), 32=>64, stride=1, relu),
   # Camada 4: 10x10 => 8x8
   Conv((3, 3), 64=>64, stride=1, relu, bias=false),
   # Camada 5
   BatchNorm(64, relu),
   # 8x8 => 4x4
   MaxPool((2,2)),
   Dropout(0.25),
   # 1024 = 64x4x4 -> faz um vetor com os dados recebidos
   Flux.flatten,
   # Camada 6 -> 1024 => 256, muda de 1024 para 256
   Dense(1024, 256, bias=false),
   # Camada 7
   BatchNorm(256, relu),
   # Camada 8
   Dense(256, 128, bias=false),
   # Camada 9
   BatchNorm(128, relu),
   # Camada 10
   Dense(128, 84, bias=false),
   # Camada 11
   BatchNorm(84, relu),
   Dropout(0.25),
   # Cada saída é uma classificação
   Dense(84, 10),
   # Classificador na saída
   Flux.softmax
)

acuracia(ŷ, y) = (mean(Flux.onecold(ŷ) .== Flux.onecold(y)));
perda(x, y)    = Flux.crossentropy(modelo(x), y);

opt = Flux.ADAM(3e-5);  # taxa de aprendizagem
ps  = Flux.params(modelo);

num_épocas = 11
melhor_acu = 0.0
última_melhoria = 0

for época in 1:num_épocas

   # escritas locais a variaveis globais precisam do escopo global nos loops for por este criar um novo escopo
   global melhor_acu
   global última_melhoria

   println("Época ", época)
   Flux.train!(perda, ps, dados_treino, opt)

   # Calcule a acurácia:
   ŷteste = modelo(x_teste)
   acu = acuracia(ŷteste, y_teste)

   @info(@sprintf("[%d]: Acurácia nos testes: %.4f", época, acu))

   # Se a acurácia for muito boa, termine o treino
   if acu >= 0.999
      @info(" -> Término prematuro: alcançamos uma acurácia de 99.9%")
      break
   end
   
   # Se isto é a melhor acurácia vista até agora, salve o modelo
   if acu >= melhor_acu
      @info(" -> Uma nova melhor acurácia! Salvando o modelo para mnist_conv.bson", melhor_acu, acu)
      BSON.@save joinpath("./", "mnist_conv.bson") params=ps época acu
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

# BSON.@load joinpath("./", "mnist_conv.bson") ps
# Carregando os parâmetros no modelo
# Flux.loadparams!(modelo, ps)

ŷtreino =   modelo(x_treino)
ŷteste  =   modelo(x_teste)

acuracia(ŷtreino, y_treino)
acuracia(ŷteste, y_teste)

Flux.onecold(y_treino[:,2]) - 1 # rótulo da amostra 2
plot(Gray.(x_treino[:,:,1,2])) # imagem da amostra 2

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