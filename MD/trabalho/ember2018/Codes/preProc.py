import json


# Le o arquivo, retira elementos com label -1 e retorna a lista de dicionários
def ler_arquivo_jsonl(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        resultado = []
        for linha in linhas:
            result = json.loads(linha)
            label = result['label']
            if label != -1:
                resultado.append(result)
        return resultado


# Coloca o dicionario em uma lista, onde para cada chave será uma lista de seus respectivos valores
def separar_chaves_valores(dictionary):
    values = []
    for value in dictionary.values():
        if isinstance(value, dict):
            values.extend(separar_chaves_valores(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    values.extend(separar_chaves_valores(item))
                else:
                    values.append(item)
        else:
            values.append(value)
    return values


# Não usada, conta o numero de valores para cada chave em um dicionário
def contar_valores(json_data):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data
    lista_contagem = []
    for chave in data:
        valor = data[chave]
        if isinstance(valor, list):
            quantidade_valores = len(valor)
        else:
            quantidade_valores = 1
        lista_contagem.append(quantidade_valores)
    return lista_contagem


# Salva o label da lista de dicionarios em uma nova lista (apenas os valores)
def salvar_rotulo(lista):
    rot = []
    for elemento in lista:
        elem = elemento['label']
        rot.append(elem)
    return rot


# Remove as 5 primeiras e ultimas classes (sha256, md5, appeared, label, avclass, header, section, imports, exports, datadirectories)
def remover_categorias(dicio):
    chaves = list(dicio.keys())
    valores = list(dicio.values())
    del chaves[:5]
    del chaves[-5:]
    del valores[:5]
    del valores[-5:]
    novodict = dict(zip(chaves, valores))
    return novodict
