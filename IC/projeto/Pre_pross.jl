using Images

dir_imgs_database = "archive/"
dir_imgs_database_train = string(dir_imgs_database, "seg_train/")
dir_imgs_database_test = string(dir_imgs_database, "seg_test/")

dir_imgs_pre_processadas = "pre-proc/"
dir_imgs_pre_processadas_train = string(dir_imgs_pre_processadas, "seg_train/")
dir_imgs_pre_processadas_test = string(dir_imgs_pre_processadas, "seg_test/")

quantidade_imagens = 0

# Preprocessa uma imagem
function preprocessa_img(img)

    global quantidade_imagens = quantidade_imagens + 1

    img_redm = imresize(img, (28, 28))
    return img_redm
end

# Preprocessa as imagens de um diretorio/classe
function preprocessa_pasta_imgs(pasta_imgs::String, pasta_pre_imgs::String)
    
    # Preprocessa e salva as imagens
    nome_imgs = readdir(pasta_imgs)
    for nome_img in nome_imgs
        img = preprocessa_img(load(string(pasta_imgs, nome_img)))
        save(string(pasta_pre_imgs, nome_img), colorview(RGB, img))
    end

    return nothing
end

# Preprocessa todas as classes
function preprocessa_todas_imgs()

    if !isdir(dir_imgs_pre_processadas)
        mkdir(dir_imgs_pre_processadas)
        mkdir(dir_imgs_pre_processadas_train)
        mkdir(dir_imgs_pre_processadas_test)
    end

    classes = readdir(dir_imgs_database_train)

    for classe in classes

        # cria as pastas de treinamento e teste
        mkdir(string(dir_imgs_pre_processadas_train, classe))
        mkdir(string(dir_imgs_pre_processadas_test, classe))

        # faz o preprocessamento de dados de treino e teste
        preprocessa_pasta_imgs(
            string(dir_imgs_database_train, classe, "/"),
            string(dir_imgs_pre_processadas_train, classe, "/"))
        preprocessa_pasta_imgs(
            string(dir_imgs_database_test, classe, "/"),
            string(dir_imgs_pre_processadas_test, classe, "/"))
        
    end

    return nothing
    
end

preprocessa_todas_imgs()
println(quantidade_imagens)