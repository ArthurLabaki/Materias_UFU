from hill_climbing import *
from hill_climbing_re_al import *
from simulated_annealing import *
from profundidade_iterativa import *
import numpy as np
import time

nqueen = int(input("Escolha o N do problema das N rainhas: "))
mat = np.zeros([nqueen, nqueen], dtype='int64')

# Alunos:
# Arthur do Prado Labaki     - 11821BCC017
# Vinnicius Pereira da Silva - 11821BCC046

print("Selecione o algoritimo:")
print("1 - Busca em Profundidade Iterativa")
print("2 - Subida de Encosta (hill climbing)")
print("3 - Recristalização Simulada (simulated annealing)")

selectedNum = input()

if(selectedNum == '1'):
    print("Exibindo Busca em Profundidade Iterativa:")
    start = time.time()
    resposta = profundidadeIterativa(mat, nqueen)
    end = time.time()
    print("Tempo de execução do algoritmo: ", end-start)

elif (selectedNum == '2'):
    print("\nCom ou sem Recomeço Aleatório?")
    print("1 - Com")
    print("2 - Sem")
    selectedNum = input()

    if selectedNum == '1':
        print("\nExibindo Subida de Encosta:")
        start = time.time()
        resposta = hillClimbing1(mat, nqueen)
        end = time.time()
        print("Tempo de execução do algoritmo: ", end-start)

    elif selectedNum == '2':
        print("\nExibindo Subida de Encosta:")
        start = time.time()
        resposta = hillClimbing(mat, nqueen)
        end = time.time()
        print("Tempo de execução do algoritmo: ", end-start)

    else:
        print("Digite um número válido da próxima vez '-'")

elif (selectedNum == "3"):
    print("Exibindo Recristalização Simulada:")
    start = time.time()
    resposta = simulatedAnneling(mat, nqueen)
    end = time.time()
    print("Tempo de execução do algoritmo: ", end-start)
else:
    print("Digite um número válido da próxima vez '-'")
