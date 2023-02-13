import json

MAX_ITERATIONS = 500

def eh_cadeia(alfa, cad):
    for i in cad:
        if i not in alfa:
            return -1

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


def criar_fita(cad, branco):
    fita = branco
    for i in cad:
        fita = fita + [i]
    fita = fita + branco
    while 1:
        if len(fita) < 10:
            fita = fita + branco
        else:
            return fita


def eh_final(est, est_fin, process, out_file, dict, fita, aux):
    for i in range(0, len(est_fin)):
        if est == est_fin[i]:
            process = process + \
                [{'cadeia': fita, 'transicao_usada': 'aceita','estado_atual': est, 'posicao_fita': aux}]
            dict1 = {'processamento': process}
            dict.update(dict1)
            json.dump(dict, out_file, indent=6)
            return 0
    return 1


def transicoes(transi, estado, elem):
    for i in range(len(transi)): # todas as transições
        tran = transi[i]
        if tran[0] == estado and tran[1] == elem:  # encontrou transição
            estado = tran[2]  # ir para estado
            elem = tran[3]  # escrever elemento
            dire = tran[4]
            t = tran
            return estado, elem, dire, i
    return 0, 0, -1, 0


def mt_process(est, alfa, alfa_f, transi, est_ini, branco, est_fin, cad):

    est_inicial = est_ini[0]
    aux = 1  # ponteiro da fita
    fita = criar_fita(cad, branco)

    out_file = open("Ex-process.json", "w")
    dict = criaJson(transi)
    process = [
        {'cadeia': fita, 'transicao_usada': 'inicial','estado_atual': est_inicial, 'posicao_fita': aux}]

    j = eh_cadeia(alfa, cad)
    if j == -1:
        process = process + [
            {'cadeia': fita, 'transicao_usada': 'rejeitada','estado_atual': est_inicial,'posicao_fita': aux}]
        dict1 = {'processamento': process}
        dict.update(dict1)
        json.dump(dict, out_file, indent=6)
        out_file.close()
        return

    iterations = 0
    while 1:
        
        j = eh_final(est_inicial, est_fin, process, out_file, dict, fita, aux)
        
        if j == 0:
            out_file.close()
            return

        fita = fita.copy()
        est_inicial, fita[aux], dire, t = transicoes(transi, est_inicial, fita[aux])
        
        if iterations > MAX_ITERATIONS:
            process = process + [
                {'cadeia': fita, 'transicao_usada': 'rejeitada','estado_atual': est_inicial, 'posicao_fita': aux}]
            dict1 = {'processamento': process}
            dict.update(dict1)
            json.dump(dict, out_file, indent=6)
            out_file.close()
            return

        elif dire == 'R' or dire == 'D':
            aux = aux+1
            fita, aux = add_branco(fita, aux, branco)

        elif dire == 'L' or dire == 'E':
            aux = aux-1
            fita, aux = add_branco(fita, aux, branco)

        else:
            process = process + [
                {'cadeia': fita, 'transicao_usada': 'rejeitada','estado_atual': est_inicial, 'posicao_fita': aux}]
            dict1 = {'processamento': process}
            dict.update(dict1)
            json.dump(dict, out_file, indent=6)
            out_file.close()
            return

        x = {'cadeia': fita, 'transicao_usada': t,'estado_atual': est_inicial, 'posicao_fita': aux}
        
        process = process + [x]

        iterations = iterations+1

def criaJson(transi):
    lst = []
    for i in range(0, len(transi)):
        txt = 'T(' + transi[i][0] + ', ' + transi[i][1] + ') = (' + \
            transi[i][2] + ', ' + transi[i][3] + ', ' + transi[i][4] + ')'
        lst = lst + [txt]
    dict = {'transicoes': lst}
    return dict