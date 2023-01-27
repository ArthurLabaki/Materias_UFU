import socket
import json
import sys

# inseri cliente
def insereCli(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'ic'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# modifica cliente
def modificaCli(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'mc'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# exclui cliente
def excluiCli(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'ec'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# busca cliente
def buscaCli(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'bc'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# inseri produto
def inserePro(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'ip'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# modifica produto
def modificaPro(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'mp'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# exclui produto
def excluiPro(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'ep'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# busca produto
def buscaPro(dict):
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    cli = 'bp'+json.dumps(dict)
    s.send(cli.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()

# interface adm
if __name__ == '__main__':

    port = int(input("Porta do socket adm-admPortal (default 12345): "))

    while 1:
        print('\n============= Painel de Administrador =============')
        print("Comandos para clientes ou produtos: cliente, produto, sair ")
        comando = input("Comando: ")

        if comando == 'cliente' or comando == '1':
            print('Comandos para clientes: inserir, modificar, excluir, buscar, voltar')
            comando = input("Comando: ")

            if comando == "inserir" or comando == '1':
                print("Comando INSERIR digitado\n")
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o cpf/cnpj do cliente: ")
                tel = input("Digite o telefone do cliente: ")
                CID = cpf  # CID = CPF, pois é unico
                dict = {CID: {'Nome': nome, 'Cpf': cpf, 'Telefone': tel}}
                insereCli(dict)

            elif comando == "modificar" or comando == '2':
                print("Comando MODIFICAR digitado\nOBS: Não é possível mudar o cpf, favor exluir e recriar cliente caso necessário\n")
                CID = input("Digite o CID do cliente: ")
                nome = input("Digite o novo nome do cliente: ")
                cpf = CID
                tel = input("Digite o novo telefone do cliente: ")
                dict = {CID: {'Nome': nome, 'Cpf': cpf, 'Telefone': tel}}
                modificaCli(dict)

            elif comando == "excluir" or comando == '3':
                print("Comando EXCLUIR digitado\n")
                CID = input("Digite o CID do cliente: ")
                dict = {CID: {'Nome': 0, 'Cpf': 0, 'Telefone': 0}}
                excluiCli(dict)

            elif comando == "buscar" or comando == '4':
                print("Comando BUSCAR digitado\n")
                CID = input("Digite o CID do cliente: ")
                dict = {CID: {'Nome': 0, 'Cpf': 0, 'Telefone': 0}}
                buscaCli(dict)

            elif comando == "voltar" or comando == '5':
                print("Voltando")
            else:
                print("Comando invalido, voltando")

        elif comando == 'produto' or comando == '2':
            print('Comandos para produtos: inserir, modificar, excluir, buscar, voltar')
            comando = input("Comando: ")

            if comando == 'inserir' or comando == '1':
                print("Comando INSERIR digitado\n")
                nome = input("Digite o nome do produto: ")
                desc = input("Digite a descrição do produto: ")
                qnt = int(input("Digite a quantidade do produto, em inteiro: "))
                val = float(input("Digite o valor do produto: "))
                PID = nome  # PID = nome, pois deve ser unico
                dict = {PID: {'Nome': nome, 'Descricao': desc,
                              'Quantidade': qnt, 'Valor': val}}
                inserePro(dict)

            elif comando == 'modificar' or comando == '2':
                print("Comando MODIFICAR digitado\nOBS: Não é possível mudar o nome do produto, favor exluir e recriar produto caso necessário\n")
                PID = input("Digite o PID do produto: ")
                desc = input("Digite a nova descrição do produto: ")
                qnt = int(input("Digite a nova quantidade do produto: "))
                val = float(input("Digite o novo valor do produto: "))
                dict = {PID: {'Nome': PID, 'Descricao': desc,
                              'Quantidade': qnt, 'Valor': val}}
                modificaPro(dict)

            elif comando == 'excluir' or comando == '3':
                print("Comando EXCLUIR digitado\n")
                PID = input("Digite o PID do produto: ")
                dict = {PID: {'Nome': 0, 'Descricao': 0,
                              'Quantidade': 0, 'Valor': 0}}
                excluiPro(dict)

            elif comando == "buscar" or comando == '4':
                print("Comando BUSCAR digitado\n")
                PID = input("Digite o PID do produto: ")
                dict = {PID: {'Nome': 0, 'Cpf': 0, 'Telefone': 0}}
                buscaPro(dict)

            elif comando == "voltar" or comando == '5':
                print("Voltando")
            else:
                print("Comando invalido, voltando")

        elif comando == 'sair' or comando == '3':
            print("Saindo")
            break
        else:
            print("Comando invalido, voltando")
