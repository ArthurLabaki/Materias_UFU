from random import randint


def posicoesRainha1(tabuleiro, n):
    lst = []
    for i in range(1, n+1):
        for linha in range(len(tabuleiro)):
            for coluna in range(len(tabuleiro[linha])):
                if tabuleiro[linha][coluna] == i:
                    lst = lst + [[linha, coluna]]
    return lst


def calculaPontuacaoIndividualRainha1(posicaoRainha, tabuleiro, n):
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


def calculaPontuacaoTodaslRainhas1(posicao, estadoInicial, n):
    listaDeConflitos = []
    listafinal = []
    for i in range(0, n):
        listaDeConflitos = listaDeConflitos + \
            calculaPontuacaoIndividualRainha1(posicao[i], estadoInicial, n)
    # Removendo conflitos redundates

    for j in listaDeConflitos:
        conflitoInverso = [j[1], j[0]]
        if conflitoInverso in listaDeConflitos:
            listaDeConflitos.remove(conflitoInverso)

    return len(listaDeConflitos)


def calculaMelhorTabuleiro1(tabuleiroRaiz, n):
    tabuleirosComPontuacao = []
    for i in range(0, n):
        estadoInicial = tabuleiroRaiz.copy()
        # zerando coluna
        for j in range(0, n):
            estadoInicial[j][i] = 0

        for k in range(0, n):
            estadoInicial[k][i] = i+1
            estadoCopia = estadoInicial.copy()
            posicoesRainhas = posicoesRainha1(estadoCopia, n)
            pontuacao = calculaPontuacaoTodaslRainhas1(
                posicoesRainhas, estadoCopia, n)
            tabuleirosComPontuacao = tabuleirosComPontuacao + \
                [[estadoCopia, pontuacao]]
            estadoInicial[k][i] = 0

    posiRainhasRaiz = posicoesRainha1(tabuleiroRaiz, n)
    pontuacaoRaiz = calculaPontuacaoTodaslRainhas1(
        posiRainhasRaiz, tabuleiroRaiz, n)
    escolhido = []
    for index in range(0, len(tabuleirosComPontuacao)):
        if tabuleirosComPontuacao[index][1] < pontuacaoRaiz:
            escolhido = tabuleirosComPontuacao[index]
    if escolhido == []:
        return [tabuleiroRaiz, pontuacaoRaiz, 'Pai']
    else:
        return [escolhido[0], escolhido[1], "Filho"]


def criarTabuleiroAleatório(tabuleiro, n):
    # preecher tabuleiro com  n rainha em posição aleatória
    estadoInicial = []
    estadoInicial = tabuleiro.copy()
    for i in range(0, n):

        posicaoMatrizVertical = randint(0, 100000) % n
        estadoInicial[posicaoMatrizVertical][i] = i+1
    return estadoInicial


def hillClimbing1(tabuleiro, n):
    estadoInicial = criarTabuleiroAleatório(tabuleiro, n)
    print('\nTabuleiro Inicial: \n', estadoInicial, '\n')
    escolhido = calculaMelhorTabuleiro1(estadoInicial,  n)
    i = 0
    melhor = escolhido.copy()
    while i < 100:
        if escolhido[1] == 0:
            print('Ultimo tabuleiro escolhido: \n',
                  escolhido[0], '\nCom', escolhido[1], "colisão/ões \n")
            return escolhido[0]
        elif escolhido[2] == 'Filho':
            print('Proximo tabuleiro escolhido: \n', escolhido[0], '\n')
            escolhido = calculaMelhorTabuleiro1(escolhido[0],  n)
        else:
            if escolhido[1] < melhor[1]:
                melhor = escolhido
            estadoInicial = criarTabuleiroAleatório(tabuleiro, n)
            print('Recriando tabuleiro: \n', estadoInicial, '\n')
            escolhido = calculaMelhorTabuleiro1(estadoInicial,  n)
        i = i + 1
    print('Ultimo tabuleiro escolhido: \n',
          melhor[0], '\nCom', melhor[1], "colisão/ões \n")
    return melhor[0]
