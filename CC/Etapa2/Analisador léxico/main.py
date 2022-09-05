from anlex import *

arq = open("codigo.txt", "r")  # abre arquivo
stri = []
i = 1
while 1:

    (nome, atr, (linha, coluna)) = buscar_token(arq, i)
    if nome == 'ERRO':
        print(f"Erro encontrado na linha {linha} e coluna {coluna}")
        break
    if atr == NULL:
        atr = '-'
    if nome == 'EOF':
        break
    print(f"Nome: {nome} | Atr: {atr}")
    stri = stri + [(nome, atr)]
    i += 1
    arq.seek(0, 0)
print(stri)

arq.close()
