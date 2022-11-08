from random import randint as randint
import random
from math import exp


def posicoesRainha(tabuleiro, n):
    listaDePosicoesDaRainhas = []
    for i in range(1, n+1):
        for linha in range(len(tabuleiro)):
            for coluna in range(len(tabuleiro[linha])):
                if tabuleiro[linha][coluna] == i:
                    listaDePosicoesDaRainhas = listaDePosicoesDaRainhas + \
                        [[linha, coluna]]
    return listaDePosicoesDaRainhas


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


def criarTabuleiroAleatório(tabuleiro, n):
    # preecher tabuleiro com  n rainha em posição aleatória
    estadoInicial = []
    estadoInicial = tabuleiro.copy()
    for i in range(0, n):

        posicaoMatrizVertical = randint(0, 100000) % n
        estadoInicial[posicaoMatrizVertical][i] = i+1
    return estadoInicial


def simulatedAnneling(tabuleiro, n):
    estadoInicial = criarTabuleiroAleatório(
        tabuleiro, n)  # <- tabuleiro inicial
    print('\nTabuleiro Inicial: \n', estadoInicial, '\n')

    temperatura = 4000
    resfriamento = 0.99

    while temperatura > 0:
        #print("Temperatura atual: ", temperatura, "\n")

        posicoesRainhas = posicoesRainha(estadoInicial, n)
        pontuacaoRaiz = calculaPontuacaoTodaslRainhas(
            posicoesRainhas, estadoInicial, n)

        while 1:
            rainhaAleatoria = (randint(0, 100000) %
                               n)  # Pega uma rainha aleatoria
            # Pega uma posicao para colocar a rainha gerada aleatoriamente
            posicaoAleatoriaDaRainha = randint(0, n - 1)
            # Checa se a posicao da rainha gerada aleatoriamente nao é a posicao que ela esta atualmente
            if posicaoAleatoriaDaRainha != posicoesRainhas[rainhaAleatoria][0]:
                break
        estadoAleatorio = estadoInicial.copy()
        estadoAleatorio[posicoesRainhas[rainhaAleatoria]
                        [0]][posicoesRainhas[rainhaAleatoria][1]] = 0  # Apaga a rainha
        estadoAleatorio[posicaoAleatoriaDaRainha][posicoesRainhas[rainhaAleatoria]
                                                  [1]] = rainhaAleatoria + 1  # Coloca a rainha na nova posicao
        posicoesRainhasAleatorias = posicoesRainha(estadoAleatorio, n)
        pontuacaoAleatoria = calculaPontuacaoTodaslRainhas(
            posicoesRainhasAleatorias, estadoAleatorio, n)

        delta = pontuacaoAleatoria - pontuacaoRaiz

        if pontuacaoAleatoria == 0:
            print('Ultimo tabuleiro escolhido: \n',
                  estadoAleatorio, "\nCom 0 colisão/ões \n")
            return estadoAleatorio

        if (delta < 0) or random.uniform(0, 1) < exp(-delta / temperatura):
            print('Novo tabuleiro escolhido: \n', estadoAleatorio,
                  "\nCom", pontuacaoAleatoria, "colisão/ões \n")
            estadoInicial = estadoAleatorio
        else:
            print("Vizinho aleatório rejeitado\n")

        temperatura = temperatura * resfriamento
    print('Ultimo tabuleiro escolhido: \n',
          estadoInicial, "\nCom", pontuacaoRaiz, "colisão/ões \n")
    return estadoInicial
