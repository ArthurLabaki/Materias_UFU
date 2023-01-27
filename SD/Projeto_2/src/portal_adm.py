from cache import Cache

import socket
import json
import sys

# inserir pedido
def retornaChaveValor(msg):
    return list(msg.keys())[0], list(msg.values())[0]

# inseri cliente
def insereCli(msg):
    msg = json.loads(msg)
    chave, valor = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            resp2 = enviarMsgReplica('c', chave, valor)
            if resp2['status'] == 'OK':
                return "Cliente "+ chave +" criado com sucesso"
            else:
                return str(resp2['resposta'])
        else:
            return "Cliente já cadastrado " + str(resp['resposta'])
    else:
        return str(resp['resposta'])

# modifica cliente
def modificaCli(msg):
    msg = json.loads(msg)
    chave, valor = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Cliente "+ chave +" não existe"
        else:
            resp2 = enviarMsgReplica('u', chave, valor)
            if resp2['status'] == 'OK':
                return "Cliente "+ chave +" modificado com sucesso"
            else:
                return str(resp2['resposta'])
    else:
        return str(resp['resposta'])
                
# exclui cliente
def excluiCli(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Cliente "+ chave +" não existe"
        else:
            resp2 = enviarMsgReplica('d', chave)
            if resp2['status'] == 'OK':
                return "Cliente "+ chave +" excluido com sucesso"
            else:
                return str(resp2['resposta'])
    else:
        return str(resp['resposta'])
        
# busca cliente
def buscaCli(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Cliente "+ chave +" não existe"
        else:
            return "Cliente: " + str(resp['resposta'])
    else:
        return str(resp['resposta'])

# inseri produto
def inserePro(msg):
    msg = json.loads(msg)
    chave, valor = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            resp2 = enviarMsgReplica('c', chave, valor)
            if resp2['status'] == 'OK':
                return "Produto "+ chave +" criado com sucesso"
            else:
                return str(resp2['resposta'])
        else:
            return "Produto já cadastrado " + str(resp['resposta'])
    else:
        return str(resp['resposta'])

# modifica produto
def modificaPro(msg):
    msg = json.loads(msg)
    chave, valor = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Produto "+ chave +" não existe"
        else:
            resp2 = enviarMsgReplica('u', chave, valor)
            if resp2['status'] == 'OK':
                return "Produto "+ chave +" modificado com sucesso"
            else:
                return str(resp2['resposta'])
    else:
        return str(resp['resposta'])

# exclui produto
def excluiPro(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Produto "+ chave +" não existe"
        else:
            resp2 = enviarMsgReplica('d', chave)
            if resp2['status'] == 'OK':
                return "Produto "+ chave +" excluido com sucesso"
            else:
                return str(resp2['resposta'])
    else:
        return str(resp['resposta'])

# busca produto
def buscaPro(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Produto "+ chave +" não existe"
        else:
            return "Produto: " + str(resp['resposta'])
    else:
        return str(resp['resposta'])

# para testar o cache
def imprimirCache():

    global AdmCache

    print('\n')
    for chave in AdmCache.cacheHashTable:
        print('  ', chave, ' : ', AdmCache.cacheHashTable[chave])
    print('\n')

# Circularmente escolhe replicas validas
def escolheReplicaValida():

    global NumReplica, SocketRepl

    inativas = 1
    while True:
        if inativas >= 3:
            print('Replicas inativas, fechando o programa')
            sys.exit()
        
        # Tenta acessar as réplicas circularmente [0,2]
        NumReplica = (NumReplica+1)%3 # 0,1 -> 1,2 -> 2,1,0
        deuExcept = False
        try:

            # tenta conectar a nova replica
            SocketRepl = socket.socket()
            host = socket.gethostname()
            if NumReplica == 0:
                SocketRepl.connect((host, 6010))
            elif NumReplica == 1:
                SocketRepl.connect((host, 6011))
            else:
                SocketRepl.connect((host, 6012))
            print('Replica ' + str(NumReplica) + ' escolhida!')

        except BaseException as e:
            deuExcept = True

        if not deuExcept:
            break

        inativas = inativas+1

# envia uma requisição para as replicas por socket
def enviarMsgReplica(funcao, chave, valor=None):

    global AdmCache, SocketRepl

    # Se for read tenta acessar o cache
    if funcao == 'r':
        valorC = AdmCache.ler(chave)
        if valorC != None:
            print('Mensagem retornada pelo cache')
            return {'status': 'OK', 'resposta': valorC }

    msgTmp = json.dumps({'funcao': funcao, 'chave': chave, 'valor': json.dumps(valor)})
    resp = None
    
    try:
        SocketRepl.send(msgTmp.encode()) 
        resp = SocketRepl.recv(10240)
    except BaseException as e:
        # no caso de replica inativa, escolhe uma nova e reenvia a requisicao
        if type(e) == ConnectionResetError:
            escolheReplicaValida()
            SocketRepl.send(msgTmp.encode()) 
            resp = SocketRepl.recv(10240)
        else:
            print('Falha ' + str(e))
            sys.exit()

    respJson = json.loads(resp.decode())

    # Atualiza o cache se a requisicao deu certo
    if respJson['status'] == 'OK' and respJson['resposta'] != 'None' and respJson['resposta'] != None:
        if funcao == 'c':
            AdmCache.inserir(chave, valor)
            print('CACHE: Inserido', chave, valor)
        if funcao == 'r':
            AdmCache.inserir(chave, respJson['resposta'])
            print('CACHE: Inserido', chave, respJson['resposta'])
        if funcao == 'u':
            AdmCache.inserir(chave, valor)
            print('CACHE: Atualizado', chave, valor)
        if funcao == 'd':
            AdmCache.inserir(chave, None)
            print('CACHE: Deletado', chave)

    return respJson

if __name__ == '__main__':

    # globais
    NumReplica = 0
    SocketRepl = None
    AdmCache = Cache()

    # Conectar no socket das replicas
    escolheReplicaValida()

    # Conectar no socket adm/admPortal
    porta = int(input("Porta do socket adm/admPortal (default 12345): "))
    try:
        sPor = socket.socket()
        host = socket.gethostname()
        sPor.bind((host, porta))
    except:
        print('Falha ao se conectar ao socket \nFinalizando programa!')
        sys.exit()
    sPor.listen(20)
    print('Portal inicializado, aguardando por mensagens...')

    while True:
        status = 1
        c, addr = sPor.accept()
        data = c.recv(1024)
        msg = data.decode()

        if msg[1] == "c":
            # Inserir Cliente
            if msg[0] == "i":
                status = insereCli(msg[2:])
                print(status)
                c.send(status.encode())

            # Modificar Cliente
            elif msg[0] == "m":
                status = modificaCli(msg[2:])
                print(status)
                c.send(status.encode())
            
            # Excluir Cliente
            elif msg[0] == "e":
                status = excluiCli(msg[2:])
                print(status)
                c.send(status.encode())

            # Buscar Cliente
            elif msg[0] == "b":
                status = buscaCli(msg[2:])
                envio = 'Busca de cliente realizada!\n' + status
                print(envio)
                c.send(envio.encode())
            else:
                c.send('Operação falhada!'.encode())

        elif msg[1] == "p":

            # Inserir Produto
            if msg[0] == "i":   
                status = inserePro(msg[2:])
                print(status)
                c.send(status.encode())

            # Modificar Produto
            elif msg[0] == "m":
                status = modificaPro(msg[2:])
                print(status)
                c.send(status.encode())

            # Excluir Produto
            elif msg[0] == "e":
                status = excluiPro(msg[2:])
                print(status)
                c.send(status.encode())

            # Buscar Produto
            elif msg[0] == "b":
                status = buscaPro(msg[2:])
                envio = 'Busca de produto realizada!\n' + status
                print(envio)
                c.send(envio.encode())
            else:
                c.send('Operação falhada!'.encode())
        else:
            print('Operação falhada!')
            c.send('Operação falhada!'.encode())

        c.close()
