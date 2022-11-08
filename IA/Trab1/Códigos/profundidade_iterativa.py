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


def calculaVizinhos(tabuleiroRaiz, n):
    tabuleirosComPontuacao = []
    for i in range(0, n):
        estadoInicial = tabuleiroRaiz.copy()
        # zerando coluna
        for j in range(0, n):
            if estadoInicial[j][i] != 0:
                rainha, linha, coluna = estadoInicial[j][i], j, i
            estadoInicial[j][i] = 0

        for k in range(0, n):
            if k == linha and i == coluna:
                print("", end='')
            else:
                estadoInicial[k][i] = i+1
                estadoCopia = estadoInicial.copy()
                posicoesRainhas = posicoesRainha(estadoCopia, n)
                pontuacao = calculaPontuacaoTodaslRainhas(
                    posicoesRainhas, estadoCopia, n)
                tabuleirosComPontuacao = tabuleirosComPontuacao + \
                    [[estadoCopia, pontuacao]]
                estadoInicial[k][i] = 0
    return tabuleirosComPontuacao


def iteracao(estadoInicial, limiteAtual, limiteMax, n):

    posiRainhas = posicoesRainha(estadoInicial, n)
    pontuacaoRaiz = calculaPontuacaoTodaslRainhas(
        posiRainhas, estadoInicial, n)
    print('Novo tabuleiro verificado: \n', estadoInicial,
          "\nCom", pontuacaoRaiz, "colisão/ões \n")

    if pontuacaoRaiz == 0:
        return estadoInicial
    elif limiteAtual > limiteMax:
        return estadoInicial

    else:
        vizinhos = calculaVizinhos(estadoInicial, n)
        for i in range(0, len(vizinhos)):
            if vizinhos[i][1] == 0:
                return vizinhos[i][0]
            else:
                x = iteracao(vizinhos[i][0], limiteAtual+1, limiteMax, n)
                posiRainhas = posicoesRainha(x, n)
                pontuacaoRaiz1 = calculaPontuacaoTodaslRainhas(
                    posiRainhas, x, n)
                if pontuacaoRaiz1 == 0:
                    return x
    return x


def profundidadeIterativa(tabuleiro, n):
    # preecher tabuleiro com  n rainha em posição aleatória
    estadoInicial = tabuleiro
    for i in range(0, n):

        posicaoMatrizVertical = randint(0, 100000) % n
        estadoInicial[posicaoMatrizVertical][i] = i+1
    print('\nTabuleiro Inicial: \n', estadoInicial, '\n')
    limiteMax = n+1
    limiteAtual = 0
    x = iteracao(estadoInicial, limiteAtual, limiteMax, n)
    posiRainhas = posicoesRainha(x, n)
    pontuacaoRaiz = calculaPontuacaoTodaslRainhas(
        posiRainhas, x, n)
    print('Ultimo tabuleiro escolhido: \n',
          x, "\nCom", pontuacaoRaiz, "colisão/ões \n")
