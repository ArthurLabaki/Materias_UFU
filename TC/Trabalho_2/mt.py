import json

MAX_ITERATIONS = 5000

# cria a fita
def criar_fita(cadeia, branco):
    fita = branco
    for i in cadeia:
        fita = fita + [i]
    fita = fita + branco
    while 1:
        if len(fita) < 10:
            fita = fita + branco
        else:
            return fita

# criação inicial do json de saída"
def criaJson(listaEstados, alfabeto, branco, alfabeto_f1, alfabeto_f2, transicoes, estado_inicial, estado_final, cadeia1, cadeia2):
    listaDeTransicoes = []
    for i in range(0, len(transicoes)):
        txt = 'T(' + transicoes[i][0] + ', ' + transicoes[i][1] + ', ' + transicoes[i][2] + ') = (' + \
            transicoes[i][3] + ', ' + transicoes[i][4] + ', ' + transicoes[i][5] + ', ' + transicoes[i][6] + ', ' + transicoes[i][7] + ')'
        listaDeTransicoes = listaDeTransicoes + [txt]

    dicionario = {
        'estados':listaEstados, 
        'alfabeto do automato': alfabeto,
        'caractere branco': branco,
        'alfabeto da fita 1': alfabeto_f1,
        'alfabeto da fita 2': alfabeto_f2,
        'transicoes': listaDeTransicoes, 
        'estado inicial': estado_inicial, 
        'estados finais': estado_final, 
        'cadeia de entrada 1': cadeia1,
        'cadeia de entrada 2': cadeia2,

    }
    return dicionario

# verifica se a cadeia pertence ao alfabeto
def eh_cadeia(alfabeto, cadeia):
    for i in cadeia:
        if i not in alfabeto:
            return -1

# verifica se o estado atual é presente nos estados finais da MT
def eh_final(estado_atual, estado_final, processamento, out_file, dicionario, fita1, fita2, auxSeta1, auxSeta2, iterations):
    for i in range(0, len(estado_final)):
        if estado_atual == estado_final[i]:
            processamento = processamento + \
                [{'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'ACEITA','estado_atual': estado_atual, 'posicao_fita_1': auxSeta1, 'posicao_fita_2': auxSeta2}]
            dicionario1 = {'processamento': processamento, 'iterations': iterations}
            dicionario.update(dicionario1)
            json.dump(dicionario, out_file, indent=6)
            return 0 
    return 1

# adiciona branco nas extremidades caso necessário
def add_branco(fita, aux, branco):
    if aux >= len(fita):    # Adicionando para a direita
        fita = fita + branco
        return fita, aux
    elif aux < 0:           # Adicionando para a esquerda
        fita = branco + fita
        aux = aux+1
        return fita, aux
    else:
        return fita, aux

# realiza as transições
def transicionar(transicoes, estadoAtual, elementoFita1, elementoFita2):
    for index in range(len(transicoes)): # todas as transições
        transicaoIndividual = transicoes[index] # T(q0, a, b) = (q1, X, Y, R, L)",...
        if transicaoIndividual[0] == estadoAtual and transicaoIndividual[1] == elementoFita1  and  transicaoIndividual[2] == elementoFita2 :  # encontrou transição
            estadoAtual = transicaoIndividual[3]  # estado
            elementoFita1 = transicaoIndividual[4]  # elemento fita 1
            elementoFita2 = transicaoIndividual[5]  # elemento fita 2
            direcaoF1 = transicaoIndividual[6]  # direcao fita 1
            direcaoF2 = transicaoIndividual[7]  # direcao fita 2
            return estadoAtual, elementoFita1, elementoFita2 ,direcaoF1, direcaoF2, index
            
    return estadoAtual, elementoFita1, elementoFita2 ,-1, -1, index # Transicao de erro

# processamento geral da MT
def processamento_mt(estados, alfabeto, branco, alfabetoFita1, alfabetoFita2, transicoes, estado_inicial, estado_final, cadeia1, cadeia2):

    iterations = 0
    estado_atual = estado_inicial[0]
    aux1 = 1  #ponteiro da fita 1
    aux2 = 1  #ponteiro da fita 2
    fita1 = criar_fita(cadeia1, branco)
    fita2 = criar_fita(cadeia2, branco)
    
    out_file = open("Ex-process.json", "w")
    
    dict = criaJson(estados, alfabeto, branco, alfabetoFita1, alfabetoFita2, transicoes, estado_inicial, estado_final, cadeia1, cadeia2)
    process = [
        {'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'inicial','estado_atual': estado_atual, 'posicao_fita_1': aux1, 'posicao_fita_2': aux2}]

    j = eh_cadeia(alfabeto, cadeia1)
    g = eh_cadeia(alfabeto, cadeia2)
    if j == -1 or g == -1:
        process = process + [
            {'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'REJEITA','estado_atual': estado_atual,'posicao_fita_1': aux1, 'posicao_fita_2': aux2}]
        dict1 = {'processamento': process, 'iterations': iterations}
        dict.update(dict1)
        json.dump(dict, out_file, indent=6)
        out_file.close()
        return

    while 1:
        
        j = eh_final(estado_atual, estado_final, process, out_file, dict, fita1, fita2, aux1, aux2, iterations)
        
        if j == 0:
            out_file.close()
            return

        fita1 = fita1.copy()
        fita2 = fita2.copy()
        estado_atual, fita1[aux1], fita2[aux2], direF1, direF2, t = transicionar(transicoes, estado_atual, fita1[aux1], fita2[aux2])
        
        if iterations > MAX_ITERATIONS:
            process = process + [
                {'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'REJEITA','estado_atual': estado_atual,'posicao_fita_1': aux1, 'posicao_fita_2': aux2}]
            dict1 = {'processamento': process, 'iterations': iterations}
            dict.update(dict1)
            json.dump(dict, out_file, indent=6)
            out_file.close()
            return
        
        else:
            # direcoes da fita 1
            if direF1 == 'R' or direF1 == 'D':
                aux1 = aux1+1
                fita1, aux1 = add_branco(fita1, aux1, branco)

            elif direF1 == 'L' or direF1 == 'E':
                aux1 = aux1-1
                fita1, aux1 = add_branco(fita1, aux1, branco)

            elif direF1 == 'I' or direF1 == 'P':
                aux1 = aux1

            else:
                process = process + [{'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'REJEITA','estado_atual': estado_atual,'posicao_fita_1': aux1, 'posicao_fita_2': aux2}]
                dict1 = {'processamento': process, 'iterations': iterations}
                dict.update(dict1)
                json.dump(dict, out_file, indent=6)
                out_file.close()
                return
            
            if direF2 == 'R' or direF2 == 'D':
                aux2 = aux2+1
                fita2, aux2 = add_branco(fita2, aux2, branco)
            
            elif direF2 == 'L' or direF2 == 'E':
                aux2 = aux2-1
                fita2, aux2 = add_branco(fita2, aux2, branco)

            elif direF2 == 'I' or direF2 == 'P':
                aux2 = aux2

            else:
                process = process + [{'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': 'REJEITA','estado_atual': estado_atual,'posicao_fita_1': aux1, 'posicao_fita_2': aux2}]
                dict1 = {'processamento': process, 'iterations': iterations}
                dict.update(dict1)
                json.dump(dict, out_file, indent=6)
                out_file.close()
                return

        x = {'fita_1': fita1, 'fita_2': fita2, 'transicao_usada': t,'estado_atual': estado_atual,'posicao_fita_1': aux1, 'posicao_fita_2': aux2}
        
        process = process + [x]

        iterations = iterations+1