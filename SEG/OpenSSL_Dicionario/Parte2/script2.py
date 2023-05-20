'''
import subprocess
resultado = []

with open('dict2.txt') as f:
    senhas = f.read().splitlines()

for senha in senhas:
    try:
        cmd = f'openssl enc -d -aes-256-cbc -pbkdf2 -salt -in file9.enc -pass pass:{senha}'
        saida = subprocess.check_output(cmd, shell=True)
        print(f'Senha correta: {senha}')
        print('Conteúdo descriptografado:')
        print(saida.decode('latin1'))
        resultado.append((senha, saida))
    except subprocess.CalledProcessError:
        #print(f'Senha incorreta: {senha}')
        continue
print('Senha e saída descriptografada:')
for elemento in resultado:
    print(elemento)
'''

import subprocess
import os

resultado = []

with open('palavras_manual.txt') as f:
    senhas = f.read().splitlines()

for senha in senhas:
    for filename in os.listdir('arquivos'):
        if filename.startswith('file'):
            try:
                cmd = f'openssl enc -d -aes-256-cbc -pbkdf2 -salt -in "files/{filename}" -pass pass:{senha}'
                saida = subprocess.check_output(cmd, shell=True)
                print(f'Senha correta: {senha}')
                print(f'Conteúdo descriptografado do arquivo {filename}:')
                print(saida.decode('latin1'))
                resultado.append((senha, filename, saida))
            except subprocess.CalledProcessError:
                #print(f'Senha incorreta: {senha}')
                continue

print('Senha, arquivo e saída descriptografada:')
with open("ResultadoM.txt", "w") as arquivo:
    for elemento in resultado:
        arquivo.write(str(elemento) + "\n")


