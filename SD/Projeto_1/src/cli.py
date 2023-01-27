import socket
import json


def inserePed(dict):        # Inserir pedido
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    ped = 'ir'+json.dumps(dict)
    s.send(ped.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()


def modPed(dict):       # Modificar pedido
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    ped = 'mr'+json.dumps(dict)
    s.send(ped.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()


def enumall(dict):      # Enumerar todos os pedidos
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    ped = 'Er'+json.dumps(dict)
    s.send(ped.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()


def enumped(dict):      # Enumerar unico pedido
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    ped = 'er'+json.dumps(dict)
    s.send(ped.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()


def exclPed(dict):      # Excluir pedido
    try:
        s = socket.socket()
        host = socket.gethostname()
        global port
        s.connect((host, port))
    except:
        print('Falha ao se conectar ao socket, tente enviar a mensagem novamente!')
    ped = 'xr'+json.dumps(dict)
    s.send(ped.encode())
    data = s.recv(1024)
    print(data.decode())
    s.close()


if __name__ == '__main__':      # Main
    port = int(input("Porta (default 54321): "))
    while 1:
        print('\n============= Painel de Cliente =============')
        print('Comandos para pedidos: inserir, modificar, enumerar, excluir, sair')
        comando = input("Comando: ")

        if comando == "inserir" or comando == '1':
            print("Comando INSERIR digitado\n")
            CID = input("Digite o seu CID: ")
            dict = {CID: 0}
            inserePed(dict)

        elif comando == "modificar" or comando == '2':
            print("Comando MODIFICAR digitado\n")
            CID = input("Digite o seu CID: ")
            OID = input("Digite o seu OID: ")
            prod = input("Digite o nome do produto: ")
            qnt = input("Digite a quantidade do produto: ")
            ID = CID+':'+OID
            dict = {ID: {'Produto': prod, 'Quantidade': qnt}}
            modPed(dict)

        elif comando == "enumerar" or comando == '3':
            print("Comando ENUMERAR digitado\n")
            CID = input("Digite o seu CID: ")
            OID = input("Se desejar ver de um pedido, digite o OID: ")
            ID = CID+':'+OID
            dict = {ID: {}}
            if OID == '':
                enumall({CID: {}})
            else:
                enumped(dict)
        elif comando == "excluir" or comando == '4':
            print("Comando EXCLUIR digitado\n")
            CID = input("Digite o seu CID: ")
            OID = input("Digite o seu OID: ")
            ID = CID+':'+OID
            dict = {ID: {}}
            exclPed(dict)

        elif comando == 'sair' or comando == '5':
            print("Saindo")
            break
        else:
            print("Comando invalido, voltando")
