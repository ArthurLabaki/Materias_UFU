def ler_arquivo_txt(nome_arquivo):
    lista_linhas = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip() 
            lista_linhas.append(linha)
    return lista_linhas

def salvar_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for elemento in lista:
            arquivo.write(str(elemento) + '\n')

def concatenar_listas(lista1, lista2):
    return lista1 + lista2


########################################################

def converter_para_minuscula(palavras):
    palavras_minusculas = [palavra.lower() for palavra in palavras]
    return palavras_minusculas

def converter_para_maiuscula(palavras):
    palavras_minusculas = [palavra.upper() for palavra in palavras]
    return palavras_minusculas


def combinar_palavras(lista): # junção de duas palavras (a, b, aa, ab, ba, bb)
    combinacoes = []
    for palavra1 in lista:
        for palavra2 in lista:
            combinacao = palavra1 + palavra2
            combinacoes.append(combinacao)
    return combinacoes

def variacoes_maiusculo(lista): # Variações de maiusculas (casa, Casa, cAsa, caSa, casA)
    result = []
    for palavra in lista:
        variacoes = []
        for i in range(len(palavra)):
            nova_palavra = palavra[:i] + palavra[i].upper() + palavra[i+1:]
            variacoes.append(nova_palavra)
        result.extend(variacoes)
    return result

def gerar_variacoes(palavras): # Variações de maiusculas (casa, Casa, CAsa CASA, CaSA,...)
    todas_variacoes = []

    for palavra in palavras:
        print(palavra)
        variacoes = []
        n = len(palavra)
        num_combinacoes = 2 ** n  # número total de combinações possíveis
        
        for i in range(num_combinacoes):
            variacao = ""
            for j in range(n):
                if (i >> j) % 2 == 1:  # verifica se o j-ésimo bit está definido em i
                    variacao += palavra[j].upper()  # converte a letra para maiúscula
                else:
                    variacao += palavra[j].lower()  # mantém a letra como minúscula
            variacoes.append(variacao)
        todas_variacoes.extend(variacoes)
    
    return todas_variacoes

def realizar_substituicoes(palavras, substituicoes):
    palavras_modificadas = []
    for palavra in palavras:
        palavra_modificada = ""
        for letra in palavra:
            if letra.lower() in substituicoes:
                palavra_modificada += substituicoes[letra.lower()]
            else:
                palavra_modificada += letra
        palavras_modificadas.append(palavra_modificada)

    return palavras_modificadas


def realizar_substituicoes_foneticas(palavras):
    substituicoes = {
        "to": "2",
        "be": "B",
        "you": "U",
        "are": "R",
        "ate": "8",
    }

    palavras_modificadas = []
    for palavra in palavras:
        for substituicao in substituicoes:
            palavra = palavra.replace(substituicao, substituicoes[substituicao])
        palavras_modificadas.append(palavra)

    return palavras_modificadas





subst1 = {
        'a': '@',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7',
        'l': '1',
    }
subst2 = {
        'a': '@',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
subst3 = {
        'a': '@',
        'e': '3',
        'o': '0',
        's': '5',
        't': '7',
        'l': '1',
    }
subst4 = {
        'a': '@'
    }
subst5 = {
        'a': '4'
    }
subst6 = {
        'e': '3'
    }
subst7 = {
        'i': '1'
    }
subst8 = {
        'o': '0'
    }
subst9 = {
        's': '5'
    }
subst10 = {
        't': '7'
    }
subst11 = {
        'l': '1'
    }

nome_arquivo = 'palavras_minusculas.txt'
listaPalavra = ler_arquivo_txt(nome_arquivo)

resultado = combinar_palavras(listaPalavra)
resultado2 = realizar_substituicoes(resultado, subst1)
resultado1 = realizar_substituicoes_foneticas(resultado)
resultF = resultado2 + resultado1

nome_arquivo = 'palavras_comb_grafono.txt'
salvar_lista_em_arquivo(resultF, nome_arquivo)


########################################################

#nome_arquivo = 'palavras_minusculas.txt'
#listaPalavra = ler_arquivo_txt(nome_arquivo)

#resultado = combinar_palavras(listaPalavra)

#listaFinal = concatenar_listas(listaPalavra, resultado)
#nome_arquivo = 'palavras_m_combinadas.txt'
#salvar_lista_em_arquivo(listaFinal, nome_arquivo)





