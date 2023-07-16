using Images

dir_imgs_db_train = "archive/seg_train/"
dir_imgs_db_test = "archive/seg_test/"

dir_imgs_pre_process_train = "pre_process/seg_train/"
dir_imgs_pre_process_test = "pre_process/seg_test/"

img_num = 0

#Preprocessa uma imagem
function preprocessa_img(img)

    global img_num += 1

    img_redm = imresize(img, (28, 28))
    return img_redm
end

#Preprocessa as imagens de um diretorio/classe
function preprocessa_pasta_imgs(pasta_imgs::String, pasta_pre_imgs::String)
#Preprocessa e salva as imagens
    nome_imgs = readdir(pasta_imgs)
    for nome_img in nome_imgs
        img = preprocessa_img(load(string(pasta_imgs, nome_img)))
        save(string(pasta_pre_imgs, nome_img), colorview(RGB, img))
    end

    return nothing
end

#Preprocessa todas as classes
function preprocessa_todas_imgs()

    if !isdir("pre_process/")
        mkdir("pre_process/")
        mkdir(dir_imgs_pre_process_train)
        mkdir(dir_imgs_pre_process_test)
    end

    classes = readdir(dir_imgs_db_train)

    for classe in classes
        
        # cria as pastas de treinamento e teste
        mkdir(string(dir_imgs_pre_process_train, classe))
        mkdir(string(dir_imgs_pre_process_test, classe))

        # faz o preprocessamento de dados de treino e teste
        preprocessa_pasta_imgs(
            string(dir_imgs_db_train, classe, "/"),
            string(dir_imgs_pre_process_train, classe, "/"))
        preprocessa_pasta_imgs(
            string(dir_imgs_db_test, classe, "/"),
            string(dir_imgs_pre_process_test, classe, "/"))

    end

    return nothing

end

preprocessa_todas_imgs()
println(img_num)