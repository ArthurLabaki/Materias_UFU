using Flux
using Flux: onehotbatch, onecold, throttle
using Flux.Data: DataLoader
using Flux: @epochs
using Images

# Defina o caminho para o diretório onde o conjunto de dados está localizado
dataset_path = "archive"

# Carregue o conjunto de dados
function load_dataset()
    train_dir = "archive/seg_train/seg_train/"
    test_dir = "archive/seg_test/seg_test/"

    train_data = []
    train_labels = []
    test_data = []
    test_labels = []

    for (i, class_name) in enumerate(["buildings", "forest", "glacier", "mountain", "sea", "street"])
        class_train_dir = joinpath(train_dir, class_name)
        class_test_dir = joinpath(test_dir, class_name)

        for file_name in readdir(class_train_dir)
            img_path = joinpath(class_train_dir, file_name)
            img = load(img_path)
            push!(train_data, img)
            push!(train_labels, i)
        end

        for file_name in readdir(class_test_dir)
            img_path = joinpath(class_test_dir, file_name)
            img = load(img_path)
            push!(test_data, img)
            push!(test_labels, i)
        end
    end

    return train_data, train_labels, test_data, test_labels
end

# Pré-processamento dos dados
function preprocess_data(train_data, train_labels, test_data, test_labels)
    # Redimensionar as imagens para um tamanho comum
    train_data = [imresize(img, (100, 100)) for img in train_data]
    test_data = [imresize(img, (100, 100)) for img in test_data]

    # Normalização das imagens
    train_data = [Float32.(channelview(img) / 255) for img in train_data]
    test_data = [Float32.(channelview(img) / 255) for img in test_data]

    # Converter rótulos em formato one-hot
    train_labels = onehotbatch(train_labels, 1:6)
    test_labels = onehotbatch(test_labels, 1:6)

    # Criar conjuntos de dados para treinamento e teste
    train_loader = DataLoader(train_data, train_labels; batchsize=32, shuffle=true)
    test_loader = DataLoader(test_data, test_labels; batchsize=32, shuffle=true)

    return train_loader, test_loader
end

# Definir a arquitetura da CNN
function build_model()
    return Chain(
        Conv((3, 3), 3=>16, relu),
        MaxPool((2, 2)),
        Conv((3, 3), 16=>32, relu),
        MaxPool((2, 2)),
        Conv((3, 3), 32=>64, relu),
        MaxPool((2, 2)),
        x -> reshape(x, :, size(x, 4)),
        Dense(64*9*9, 128, relu),
        Dense(128, 6),
        softmax
    )
end

# Função de treinamento
function train_model(model, train_loader, test_loader, epochs)
    opt = ADAM(params(model))

    accuracy() = mean(onecold(model(x)) .== onecold(y) for (x, y) in test_loader)

    @epochs epochs Flux.train!(loss, train_loader, opt, cb=throttle(accuracy, 10))

    return model
end

# Carregar o conjunto de dados
train_data, train_labels, test_data, test_labels = load_dataset()

# Pré-processar os dados
train_loader, test_loader = preprocess_data(train_data, train_labels, test_data, test_labels)

# Construir o modelo
model = build_model()

# Definir a função de perda (loss)
loss(x, y) = Flux.crossentropy(model(x), y)

# Treinar o modelo
trained_model = train_model(model, train_loader, test_loader, 10)
