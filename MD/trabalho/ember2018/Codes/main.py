from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import numpy as np
from preProc import *
from mineracao import *

# Calcula a acuracia


def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)


def minerar(arq1, arq2, img):

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq1)
    y_train = salvar_rotulo(lista)
    X_train = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train.append(dict2)

    print('1')

    # Le o arquivo de teste e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq2)
    y_test = salvar_rotulo(lista)
    X_test = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_test.append(dict2)

    # Organiza os dados como um array estilo numpy
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    # Cria a arvore de decizão vazia
    clf = DecisionTreeClassifier()
    num_features = len(X_train[0])

    # Treina o classificador usando o conjunto de treinamento
    clf.fit(X_train, y_train)

    # Faz as previsões usando o conjunto de teste
    y_pred = clf.predict(X_test)

    # Avalia a precisão do modelo
    accuracy_score = metrics.accuracy_score(y_test, y_pred)
    print("Acuracia:", accuracy_score)

    # Criar lista de nomes de características sequenciais
    feature_names = [str(i) for i in range(1, num_features + 1)]

    # Plota a árvore de decisão
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_tree(clf, filled=True, feature_names=feature_names, ax=ax)

    # Adiciona título à figura
    ax.set_title(f"Árvore de Decisão\nPrecisão: {accuracy_score:.4f}")

    # Salva a imagem
    # plt.show()
    plt.savefig(f"arvore_De_decisão_{img}.png")


def minerarTudo(arq0, arq1, arq2, arq3, arq4, arq5, img):

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq0)
    y_train = salvar_rotulo(lista)
    X_train = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train.append(dict2)

    print('1')
    print(len(X_train))

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq1)
    y_train1 = salvar_rotulo(lista)
    X_train1 = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train1.append(dict2)

    y_train = y_train + y_train1
    X_train = X_train + X_train1

    y_train1 = []
    X_train1 = []
    print('1')
    print(len(X_train))

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq2)
    y_train1 = salvar_rotulo(lista)
    X_train1 = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train1.append(dict2)

    y_train = y_train + y_train1
    X_train = X_train + X_train1

    y_train1 = []
    X_train1 = []
    print('1')
    print(len(X_train))

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq3)
    y_train1 = salvar_rotulo(lista)
    X_train1 = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train1.append(dict2)

    y_train = y_train + y_train1
    X_train = X_train + X_train1

    y_train1 = []
    X_train1 = []
    print('1')
    print(len(X_train))

    # Le o arquivo de treino e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq4)
    y_train1 = salvar_rotulo(lista)
    X_train1 = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_train1.append(dict2)

    y_train = y_train + y_train1
    X_train = X_train + X_train1

    y_train1 = []
    X_train1 = []
    print('1')
    print(len(X_train))

    # Le o arquivo de teste e realiza o pre-processamento dele
    lista = ler_arquivo_jsonl(arq5)
    y_test = salvar_rotulo(lista)
    X_test = []
    for dicio in lista:
        dict1 = remover_categorias(dicio)
        dict2 = separar_chaves_valores(dict1)
        X_test.append(dict2)

    print('2')
    # Organiza os dados como um array estilo numpy
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    print('3')
    # Cria a arvore de decizão vazia
    clf = DecisionTreeClassifier()
    num_features = len(X_train[0])

    # Treina o classificador usando o conjunto de treinamento
    clf.fit(X_train, y_train)
    print('4')
    # Faz as previsões usando o conjunto de teste
    y_pred = clf.predict(X_test)

    # Avalia a precisão do modelo
    accuracy_score = metrics.accuracy_score(y_test, y_pred)
    print("Precisão:", accuracy_score)

    # Criar lista de nomes de características sequenciais
    feature_names = [str(i) for i in range(1, num_features + 1)]

    # Plota a árvore de decisão
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_tree(clf, filled=True, feature_names=feature_names, ax=ax)

    # Adiciona título à figura
    ax.set_title(f"Árvore de Decisão\nAcurácia: {accuracy_score:.4f}")

    # Salva a imagem
    # plt.show()
    plt.savefig(f"arvoreDeDecisão_{img}.png")


# Executa cada treino com o teste e se ocorrer um erro, passa para o proximo
try:
    minerar('train_features_0.jsonl', 'test_features.jsonl', 'train0')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'train0': {str(e)}")

try:
    minerar('train_features_1.jsonl', 'test_features.jsonl', 'train1')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'train1': {str(e)}")

try:
    minerar('train_features_2.jsonl', 'test_features.jsonl', 'train2')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'train2': {str(e)}")

try:
    minerar('train_features_3.jsonl', 'test_features.jsonl', 'train3')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'train3': {str(e)}")

try:
    minerar('train_features_4.jsonl', 'test_features.jsonl', 'train4')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'train4': {str(e)}")

try:
    minerarTudo('train_features_0.jsonl', 'train_features_1.jsonl', 'train_features_2.jsonl',
                'train_features_3.jsonl', 'train_features_4.jsonl', 'test_features.jsonl', 'trainTudo')
except Exception as e:
    print(f"Ocorreu um erro na execução da função 'trainTudo': {str(e)}")


"""


Estrutura de cada objeto json:

chave: sha256
valor: c31950077f3dc66b0decad88326773cb74102c0da3007db0c29177c5064b1269

chave: md5
valor: ba2d2b60b02cf229acd85a66284b3e43

chave: appeared
valor: 2018-09

chave: label
valor: 1

chave: avclass
valor: high

chave: histogram
valor: [39415, 6597, 5938, 5563, 5578, 6479, 5484, 4771, 6193, 7648, 4453, 5514, 5596, 6070, 5714, 5376, 6418, 5962, 5274, 5166, 4937, 5179, 4572, 4702, 4877, 6410, 4169, 5194, 6450, 5536, 4785, 5003, 5940, 6662, 5382, 4382, 5298, 5204, 5422, 4385, 4812, 4712, 5222, 5938, 5386, 5765, 4864, 4775, 5292, 5195, 4541, 4793, 5207, 4332, 5053, 3951, 4936, 4852, 3993, 5454, 5318, 4922, 4619, 4393, 5788, 6321, 5434, 5377, 9056, 5240, 4591, 5563, 5527, 6261, 4787, 8711, 6094, 6523, 5167, 5473, 5645, 5056, 4909, 4962, 5774, 4804, 4776, 4936, 4677, 5327, 5145, 6493, 5933, 5589, 5353, 5470, 5554, 4872, 4560, 4335, 5559, 5149, 4660, 4180, 4594, 4804, 5003, 5567, 5473, 5676, 5452, 6723, 5118, 4352, 4183, 5264, 5210, 4305, 4781, 4347, 5943, 4452, 3907, 4330, 5167, 4135, 5195, 4261, 4989, 4759, 4302, 6592, 5406, 3825, 4620, 4046, 4028, 5093, 5139, 5459, 5152, 4843, 4760, 5765, 5023, 5233, 4303, 5384, 5924, 5120, 5725, 5810, 4445, 5216, 4593, 5540, 7161, 4720, 4623, 4562, 5530, 4856, 3756, 4293, 4325, 5097, 4072, 6026, 5506, 4230, 4075, 4765, 4710, 5229, 6648, 4293, 5492, 4228, 4501, 4261, 4734, 4664, 4138, 4287, 5603, 4344, 4279, 4334, 5674, 4128, 6083, 4433, 5913, 5983, 5577, 5447, 6495, 5267, 5282, 4743, 4691, 5641, 4442, 5398, 5377, 4985, 6230, 6109, 5119, 5984, 5541, 4240, 6759, 4741, 6749, 4335, 4732, 5144, 5632, 5822, 4955, 4752, 6333, 5343, 4349, 5099, 4464, 3793, 5041, 4747, 5294, 3974, 4944, 4802, 4476, 4686, 5129, 4216, 5138, 4014, 4858, 6641, 3638, 5214, 5757, 6149, 4819, 4391, 5230, 6064, 5135, 5395, 4784, 4119, 3955, 4618]

chave: byteentropy
valor: [14336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5747, 29, 34, 13, 42, 23, 47, 24, 28, 13, 33, 17, 17, 25, 18, 34, 1823, 12, 16, 15, 16, 13, 21, 12, 10, 15, 10, 13, 26, 16, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2762, 79, 63, 67, 63, 57, 80, 62, 86, 69, 73, 95, 111, 118, 124, 187, 16207, 568, 450, 418, 396, 400, 552, 438, 435, 484, 452, 643, 762, 769, 1195, 2455, 5740, 283, 189, 187, 185, 191, 160, 270, 201, 242, 215, 370, 366, 347, 474, 820, 7265, 448, 372, 316, 330, 336, 291, 471, 352, 442, 385, 580, 558, 541, 661, 988, 10497, 775, 608, 563, 566, 559, 526, 1049, 660, 770, 727, 1318, 1149, 1150, 1463, 2196, 6243, 675, 513, 482, 464, 468, 543, 892, 556, 645, 593, 1189, 1026, 1030, 1332, 1781, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 181139, 166230, 165836, 151521, 189583, 167558, 161942, 146570, 155091, 163849, 152163, 146027, 170957, 168198, 142931, 152933]

chave: strings
valor: {'numstrings': 6134, 'avlength': 5.668568633844147, 'printabledist': [379, 319, 325, 318, 370, 274, 310, 288, 353, 356, 304, 381, 425, 360, 337, 329, 374, 340, 288, 346, 301, 363, 332, 322, 343, 356, 289, 327, 347, 334, 314, 381, 394, 476, 345, 421, 520, 446, 356, 400, 380, 410, 385, 528, 448, 437, 364, 410, 402, 409, 331, 402, 468, 385, 339, 381, 367, 429, 336, 430, 399, 409, 353, 366, 375, 386, 277, 345, 404, 390, 317, 316, 352, 383, 359, 396, 386, 397, 381, 396, 340, 329, 274, 284, 398, 341, 290, 351, 320, 379, 252, 335, 344, 331, 294, 338], 'printables': 34771, 'entropy': 6.57100772857666, 'paths': 0, 'urls': 0, 'registry': 0, 'MZ': 21}

chave: general
valor: {'size': 1353344, 'vsize': 3784704, 'has_debug': 0, 'exports': 0, 'imports': 8, 'has_relocations': 0, 'has_resources': 1, 'has_signature': 0, 'has_tls': 0, 'symbols': 0}

chave: header
valor: {'coff': {'timestamp': 1308078076, 'machine': 'I386', 'characteristics': ['CHARA_32BIT_MACHINE', 'RELOCS_STRIPPED', 'EXECUTABLE_IMAGE', 'LINE_NUMS_STRIPPED', 'LOCAL_SYMS_STRIPPED']}, 'optional': {'subsystem': 'WINDOWS_GUI', 'dll_characteristics': [], 'magic': 'PE32', 'major_image_version': 1, 'minor_image_version': 0, 'major_linker_version': 2, 'minor_linker_version': 25, 'major_operating_system_version': 4, 'minor_operating_system_version': 0, 'major_subsystem_version': 4, 'minor_subsystem_version': 0, 'sizeof_code': 176128, 'sizeof_headers': 4096, 'sizeof_heap_commit': 4096}}

chave: section
valor: {'entry': '', 'sections': [{'name': '', 'size': 61440, 'entropy': 7.907082960866848, 'vsize': 176128, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}, {'name': '', 'size': 0, 'entropy': -0.0, 'vsize': 8192, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}, {'name': '', 'size': 40960, 'entropy': 7.6697093044308575, 'vsize': 65536, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}, {'name': '.rsrc', 'size': 40960, 'entropy': 5.153040813942048, 'vsize': 40960, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}, {'name': '', 'size': 180224, 'entropy': 7.986451938502913, 'vsize': 2613248, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}, {'name': '.data', 'size': 876544, 'entropy': 7.980184351257665, 'vsize': 876544, 'props': ['CNT_INITIALIZED_DATA', 'MEM_EXECUTE', 'MEM_READ', 'MEM_WRITE']}]}

chave: imports
valor: {'kernel32.dll': ['GetModuleHandleA'], 'user32.dll': ['MessageBoxA'], 'advapi32.dll': ['RegCloseKey'], 'oleaut32.dll': ['SysFreeString'], 'gdi32.dll': ['CreateFontA'], 'shell32.dll': ['ShellExecuteA'], 'version.dll': ['GetFileVersionInfoA'], 'MSVBVM60.DLL': ['EVENT_SINK_GetIDsOfNames']}

chave: exports
valor: []

chave: datadirectories
valor: [{'name': 'EXPORT_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'IMPORT_TABLE', 'size': 544, 'virtual_address': 2908160}, {'name': 'RESOURCE_TABLE', 'size': 40796, 'virtual_address': 253952}, {'name': 'EXCEPTION_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'CERTIFICATE_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'BASE_RELOCATION_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'DEBUG', 'size': 0, 'virtual_address': 0}, {'name': 'ARCHITECTURE', 'size': 0, 'virtual_address': 0}, {'name': 'GLOBAL_PTR', 'size': 0, 'virtual_address': 0}, {'name': 'TLS_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'LOAD_CONFIG_TABLE', 'size': 0, 'virtual_address': 0}, {'name': 'BOUND_IMPORT', 'size': 0, 'virtual_address': 0}, {'name': 'IAT', 'size': 0, 'virtual_address': 0}, {'name': 'DELAY_IMPORT_DESCRIPTOR', 'size': 0, 'virtual_address': 0}, {'name': 'CLR_RUNTIME_HEADER', 'size': 0, 'virtual_address': 0}]
"""
