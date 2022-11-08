from random import randint


def posicoesRainha(tabuleiro, n):
    lst = []
    for i in range(1, n+1):
        for linha in range(len(tabuleiro)):
            for coluna in range(len(tabuleiro[linha])):
                if tabuleiro[linha][coluna] == i:
                    lst = lst + [[linha, coluna]]
    return lst


def calculaPontuacaoIndividualRainha(posicaoRainha, tabuleiro, n):
    linhaRainhaChecada = posicaoRainha[0]
    colunaRainhaChecada = posicaoRainha[1]

    conflitos = []

    # Checando movimento vertical
    for linha in range(0, n):
        pontuacao = 0
        elementoNaPosicao = tabuleiro[linha][colunaRainhaChecada]
        if elementoNaPosicao != 0 and elementoNaPosicao != tabuleiro[linhaRainhaChecada][colunaRainhaChecada]:
            conflitos = conflitos + \
                [[tabuleiro[linhaRainhaChecada][colunaRainhaChecada], elementoNaPosicao]]
            pontuacao = pontuacao + 1

    # Checando movimento horizontal
    for coluna in range(0, n):
        pontuacao = 0
        elementoNaPosicao = tabuleiro[linhaRainhaChecada][coluna]
        if elementoNaPosicao != 0 and elementoNaPosicao != tabuleiro[linhaRainhaChecada][colunaRainhaChecada]:
            conflitos = conflitos + \
                [[tabuleiro[linhaRainhaChecada][colunaRainhaChecada], elementoNaPosicao]]
            pontuacao = pontuacao + 1

    # Checando movimento diagonal esquerda direita
    l = linhaRainhaChecada
    c = colunaRainhaChecada
    while l > 0 and c > 0:
        l = l-1
        c = c-1
    while l < n and c < n:
        pontuacao = 0
        elementoNaPosicao = tabuleiro[l][c]
        if elementoNaPosicao != 0 and elementoNaPosicao != tabuleiro[linhaRainhaChecada][colunaRainhaChecada]:
            conflitos = conflitos + \
                [[tabuleiro[linhaRainhaChecada][colunaRainhaChecada], elementoNaPosicao]]
            pontuacao = pontuacao + 1
        l = l+1
        c = c+1

    # Checando movimento diagonal direita esquerda
    l = linhaRainhaChecada
    c = colunaRainhaChecada
    while l > 0 and c < n-1:
        l = l-1
        c = c+1
    while l < n and c > -1:
        pontuacao = 0
        elementoNaPosicao = tabuleiro[l][c]
        if elementoNaPosicao != 0 and elementoNaPosicao != tabuleiro[linhaRainhaChecada][colunaRainhaChecada]:
            conflitos = conflitos + \
                [[tabuleiro[linhaRainhaChecada][colunaRainhaChecada], elementoNaPosicao]]
            pontuacao = pontuacao + 1
        l = l+1
        c = c-1

    return conflitos


def calculaPontuacaoTodaslRainhas(posicao, estadoInicial, n):
    listaDeConflitos = []
    listafinal = []
    for i in range(0, n):
        listaDeConflitos = listaDeConflitos + \
            calculaPontuacaoIndividualRainha(posicao[i], estadoInicial, n)
    # Removendo conflitos redundates

    for j in listaDeConflitos:
        conflitoInverso = [j[1], j[0]]
        if conflitoInverso in listaDeConflitos:
            listaDeConflitos.remove(conflitoInverso)

    return len(listaDeConflitos)


def calculaMelhorTabuleiro(tabuleiroRaiz, n):
    tabuleirosComPontuacao = []
    for i in range(0, n):
        estadoInicial = tabuleiroRaiz.copy()
        # zerando coluna
        for j in range(0, n):
            estadoInicial[j][i] = 0

        for k in range(0, n):
            estadoInicial[k][i] = i+1
            estadoCopia = estadoInicial.copy()
            posicoesRainhas = posicoesRainha(estadoCopia, n)
            pontuacao = calculaPontuacaoTodaslRainhas(
                posicoesRainhas, estadoCopia, n)
            tabuleirosComPontuacao = tabuleirosComPontuacao + \
                [[estadoCopia, pontuacao]]
            estadoInicial[k][i] = 0

    posiRainhasRaiz = posicoesRainha(tabuleiroRaiz, n)
    pontuacaoRaiz = calculaPontuacaoTodaslRainhas(
        posiRainhasRaiz, tabuleiroRaiz, n)
    escolhido = []
    for index in range(0, len(tabuleirosComPontuacao)):
        if tabuleirosComPontuacao[index][1] < pontuacaoRaiz:
            escolhido = tabuleirosComPontuacao[index]
    if escolhido == []:
        return [tabuleiroRaiz, pontuacaoRaiz, 'Pai']
    else:
        return [escolhido[0], escolhido[1], "Filho"]


def hillClimbing(tabuleiro, n):
    # preecher tabuleiro com  n rainha em posição aleatória
    estadoInicial = tabuleiro
    for i in range(0, n):

        posicaoMatrizVertical = randint(0, 100000) % n
        estadoInicial[posicaoMatrizVertical][i] = i+1
    print('\nTabuleiro Inicial: \n', estadoInicial, '\n')

    escolhido = calculaMelhorTabuleiro(estadoInicial,  n)

    while 1:
        if escolhido[2] == 'Pai':
            print('Ultimo tabuleiro escolhido: \n',
                  escolhido[0], '\nCom', escolhido[1], "colisão/ões \n")
            return escolhido[0]
        else:
            print('Proximo tabuleiro escolhido: \n', escolhido[0], '\n')
            escolhido = calculaMelhorTabuleiro(escolhido[0],  n)
