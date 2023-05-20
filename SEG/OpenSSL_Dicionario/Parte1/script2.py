def uppercase_words(lst):
    uppercase_lst = list(map(str.upper, lst))
    return uppercase_lst

def lowercase_words(lst):
    lowercase_lst = list(map(str.lower, lst))
    return lowercase_lst

def capitalized_words(lst):
    capitalized_lst = list(map(str.capitalize, lst))
    return capitalized_lst

def leet(lst):
    leet_dict = {'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    leet_lst = []
    for item in lst:
        if isinstance(item, str):
            leet_item = ''
            for char in item:
                if char.upper() in leet_dict:
                    leet_item += leet_dict[char.upper()]
                else:
                    leet_item += char
            leet_lst.append(leet_item)
        else:
            leet_lst.append(item)
    return leet_lst

def inverter_palavras(lst):
    lista_invertida = []
    for palavra in lst:
        palavra_invertida = palavra[::-1] 
        lista_invertida.append(palavra_invertida)
    return lista_invertida

def transformar_palavras(lst):
    nova_lista = []
    for palavra in lst:
        palavra_transformada = ""
        for i, letra in enumerate(palavra):
            if i % 2 == 0:
                palavra_transformada += letra.upper()
            else:
                palavra_transformada += letra.lower()
        nova_lista.append(palavra_transformada)
    return nova_lista

def transformar_palavras_inv(lst):
    nova_lista = []
    for palavra in lst:
        palavra_transformada = ""
        for i, letra in enumerate(palavra):
            if i % 2 == 0:
                palavra_transformada += letra.lower()
            else:
                palavra_transformada += letra.upper()
        nova_lista.append(palavra_transformada)
    return nova_lista

def remover_espacos_lista(lst):
    lista_sem_espacos = []
    for linha in lst:
        linha_sem_espacos = linha.replace(' ', '')
        lista_sem_espacos.append(linha_sem_espacos)
    return lista_sem_espacos

def substituir_espacos_under(lst):
    lista_com_substituicao = []
    for linha in lst:
        linha_com_substituicao = linha.replace(' ', '_') 
        lista_com_substituicao.append(linha_com_substituicao)
    return lista_com_substituicao

def substituir_espacos_under_masc(lst):
    lista_convertida = []
    for frase in lst:
        palavras = frase.split()  
        frase_convertida = ''
        for palavra in palavras:
            palavra_convertida = palavra.capitalize()  
            frase_convertida += palavra_convertida + '_'
        lista_convertida.append(frase_convertida.rstrip('_'))  
    return lista_convertida

def transformar_camel_case(lst):
    lista_transformada = []
    for linha in lst:
        palavras = linha.split()
        linha_transformada = ''
        for palavra in palavras:
            if linha_transformada:
                palavra = palavra.capitalize()
            linha_transformada += palavra
        lista_transformada.append(linha_transformada)
    return lista_transformada

def transformar_camel_case_full(lst):
    lista_transformada = []
    for linha in lst:
        palavras = linha.split() 
        linha_transformada = ''
        for palavra in palavras:
            palavra_transformada = palavra.capitalize()  
            linha_transformada += palavra_transformada
        lista_transformada.append(linha_transformada)
    return lista_transformada

import unicodedata

def remover_acentos(palavras):
    palavras_sem_acentos = []
    for palavra in palavras:
        palavra_sem_acento = ''.join(
            (c for c in unicodedata.normalize('NFD', palavra) if unicodedata.category(c) != 'Mn')
        )
        if palavra_sem_acento != palavra:
            palavras_sem_acentos.append(palavra_sem_acento)
    return palavras_sem_acentos

def remover_caracteres(palavras):
    caracteres_removidos = [",", "'", ":", "-"]
    palavras_sem_caracteres = []
    
    for palavra in palavras:
        palavra_sem_caractere = palavra.replace(",", "").replace("'", "").replace(":", "").replace("-", "")
        if palavra_sem_caractere != palavra:
            palavras_sem_caracteres.append(palavra_sem_caractere)
    return palavras_sem_caracteres

import string

def remover_pontuacao(palavras):
    tabela = str.maketrans('', '', string.punctuation)
    palavras_sem_pontuacao = [palavra.translate(tabela) for palavra in palavras]
    return palavras_sem_pontuacao

def gerar_combinacoes(palavras):
    combinacoes = []
    
    for i in range(len(palavras)):
        for j in range(len(palavras)):
            if i != j:
                combinacao = str(palavras[i]) + str(palavras[j])
                combinacoes.append(combinacao)
    
    return combinacoes

def criar_variacao_maiusculo(lista_palavras):
    variacoes = []
    for palavra in lista_palavras:
        for i in range(len(palavra)):
            nova_palavra = palavra[:i] + palavra[i].upper() + palavra[i+1:]
            variacoes.append(nova_palavra)
    return variacoes

def aplicar_transformacoes(lista):
    substituicoes = {
        'a': ['@', '4'],
        'e': ['3'],
        'o': ['0'],
        's': ['$'],
        'i': ['1'],
        'l': ['1']
    }
    
    palavras_transformadas = lista.copy()
    
    for letra, transformacoes in substituicoes.items():
        palavras_temporarias = []
        
        for palavra in palavras_transformadas:
            for transformacao in transformacoes:
                palavra_transformada = palavra.replace(letra, transformacao)
                palavras_temporarias.append(palavra_transformada)
        
        palavras_transformadas.extend(palavras_temporarias)
    
    return palavras_transformadas

def substituir_letra(lista_palavras, letra_x, letra_y):
    nova_lista = []
    for palavra in lista_palavras:
        nova_palavra = palavra.replace(letra_x, letra_y)
        nova_lista.append(nova_palavra)
    return nova_lista

def substituir_caracteres(lista):
    nova_lista = ['teste']
    nova_lista.extend(substituir_letra(lista, 'a', '@'))
    nova_lista.extend(substituir_letra(lista, 'e', '3'))
    nova_lista.extend(substituir_letra(lista, 'a', '4'))
    nova_lista.extend(substituir_letra(lista, 'i', '1'))
    nova_lista.extend(substituir_letra(lista, 'l', '1'))
    nova_lista.extend(substituir_letra(lista, 'o', '0'))
    nova_lista.extend(substituir_letra(lista, 's', '$'))
    return nova_lista


def substituir_caracteres2(lista_palavras):
    substituicoes = {
        'a': '@',
        'e': '3',
        'i': '1',
        'l': '1',
        'o': '0',
        's': '$'
    }
    palavras_substituidas = []
    for palavra in lista_palavras:
        nova_palavra = ''
        for caractere in palavra:
            if caractere.lower() in substituicoes:
                nova_palavra += substituicoes[caractere.lower()]
            else:
                nova_palavra += caractere
        palavras_substituidas.append(nova_palavra)
    return palavras_substituidas


'''
with open('dict2.txt') as file1:
    senhas1 = file1.read().splitlines()

with open('palavras.txt') as file2:
    senhas2 = file2.read().splitlines()

# Aplica as funções nas senhas leet upper e lower
uppercase_lst = uppercase_words(senhas1)
lowercase_lst = lowercase_words(senhas1)
capitalized_lst = capitalized_words(senhas1)
invert_lst = inverter_palavras(senhas1)
trans_lst = transformar_palavras(senhas1)
trans2_lst = transformar_palavras_inv(senhas1)

leet_lst1 = leet(uppercase_lst)
leet_lst2 = leet(lowercase_lst)

uppercase_lstT = uppercase_words(senhas2)
lowercase_lstT = lowercase_words(senhas2)
capitalized_lstT = capitalized_words(senhas2)
invert_lstT = inverter_palavras(senhas2)
trans_lstT = transformar_palavras(senhas2)
trans2_lstT = transformar_palavras_inv(senhas2)

leet_lst1T = leet(uppercase_lstT)
leet_lst2T = leet(lowercase_lstT)


# Cria um dicionário com as listas
dictFinal = {
    'uppercase': uppercase_lst,
    'lowercase': lowercase_lst,
    'capitalized': capitalized_lst,
    'invert': invert_lst,
    'trans_1': trans_lst,
    'trans_2': trans2_lst,
    'leet1': leet_lst1,
    'leet2': leet_lst2,
    'uppercase2': uppercase_lstT,
    'lowercase2': lowercase_lstT,
    'capitalized2': capitalized_lstT,
    'invert2': invert_lstT,
    'trans_12': trans_lstT,
    'trans_22': trans2_lstT,
    'leet12': leet_lst1T,
    'leet22': leet_lst2T
}

# Escreve o dicionário no arquivo dict2.txt
with open('dictFinal.txt', 'w') as f:
    for key, value in dictFinal.items():
        f.write(f'{key}:\n')
        f.write('\n'.join(value))
        f.write('\n')


with open('dict3.txt') as file1:
    senhas = file1.read().splitlines()

lst0 = senhas
lst1 = remover_espacos_lista(senhas)
lst2 = substituir_espacos_under(senhas)
lst3 = substituir_espacos_under_masc(senhas)
lst4 = transformar_camel_case(senhas)
lst5 = transformar_camel_case_full(senhas)

list01 = uppercase_words(lst0)
list02 = lowercase_words(lst0)
list03 = capitalized_words(lst0)
list04 = inverter_palavras(lst0)
list05 = transformar_palavras(lst0)
list06 = transformar_palavras_inv(lst0)
list07 = leet(list01)
list08 = leet(list02)

list11 = uppercase_words(lst1)
list12 = lowercase_words(lst1)
list13 = capitalized_words(lst1)
list14 = inverter_palavras(lst1)
list15 = transformar_palavras(lst1)
list16 = transformar_palavras_inv(lst1)
list17 = leet(list11)
list18 = leet(list12)

list21 = uppercase_words(lst2)
list22 = lowercase_words(lst2)
list23 = capitalized_words(lst2)
list24 = inverter_palavras(lst2)
list25 = transformar_palavras(lst2)
list26 = transformar_palavras_inv(lst2)
list27 = leet(list21)
list28 = leet(list22)

list31 = uppercase_words(lst3)
list32 = lowercase_words(lst3)
list33 = capitalized_words(lst3)
list34 = inverter_palavras(lst3)
list35 = transformar_palavras(lst3)
list36 = transformar_palavras_inv(lst3)
list37 = leet(list31)
list38 = leet(list32)

list41 = uppercase_words(lst4)
list42 = lowercase_words(lst4)
list43 = capitalized_words(lst4)
list44 = inverter_palavras(lst4)
list45 = transformar_palavras(lst4)
list46 = transformar_palavras_inv(lst4)
list47 = leet(list41)
list48 = leet(list42)

list51 = uppercase_words(lst5)
list52 = lowercase_words(lst5)
list53 = capitalized_words(lst5)
list54 = inverter_palavras(lst5)
list55 = transformar_palavras(lst5)
list56 = transformar_palavras_inv(lst5)
list57 = leet(list51)
list58 = leet(list52)

# Cria um dicionário com as listas
dictFinal = {
    'l0': lst0,
    'l1': lst1,
    'l2': lst2,
    'l3': lst3,
    'l4': lst4,
    'l5': lst5,
    'l01': list01,
    'l02': list02,
    'l03': list03,
    'l04': list04,
    'l05': list05,
    'l06': list06,
    'l07': list07,
    'l08': list08,
    'l11': list11,
    'l12': list12,
    'l13': list13,
    'l14': list14,
    'l15': list15,
    'l16': list16,
    'l17': list17,
    'l18': list18,
    'l21': list21,
    'l22': list22,
    'l23': list23,
    'l24': list24,
    'l25': list25,
    'l26': list26,
    'l27': list27,
    'l28': list28,
    'l31': list31,
    'l32': list32,
    'l33': list33,
    'l34': list34,
    'l35': list35,
    'l36': list36,
    'l37': list37,
    'l38': list38,
    'l41': list41,
    'l42': list42,
    'l43': list43,
    'l44': list44,
    'l45': list45,
    'l46': list46,
    'l47': list47,
    'l48': list48,
    'l51': list51,
    'l52': list52,
    'l53': list53,
    'l54': list54,
    'l55': list55,
    'l56': list56,
    'l57': list57,
    'l58': list58  
}



listOrig = remover_acentos(senhas)
list01 = uppercase_words(listOrig)
list02 = lowercase_words(listOrig)
list03 = capitalized_words(listOrig)
list04 = inverter_palavras(listOrig)
list05 = transformar_palavras(listOrig)
list06 = transformar_palavras_inv(listOrig)
list07 = leet(list01)
list08 = leet(list02)

dictFinal = {
    'l01': list01,
    'l02': list02,
    'l03': list03,
    'l04': list04,
    'l05': list05,
    'l06': list06,
    'l07': list07,
    'l08': list08
    }
'''
with open('tot_pal.txt') as file1:
    senhas = file1.read().splitlines()
senhas2 = lowercase_words(senhas)
list0 = criar_variacao_maiusculo(senhas2)
list1 = substituir_caracteres(senhas2)
list2 = substituir_caracteres2(senhas2)
dictFinal = {
    'l0': list0,
    'l1': list1,
    'l2': list2
}

# Escreve o dicionário no arquivo dict2.txt
with open('tot_pal_comb2.txt', 'w') as f:
    for key, value in dictFinal.items():
        f.write(f'{key}:\n')
        f.write('\n'.join(value))
        f.write('\n')