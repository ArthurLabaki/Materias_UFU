import socket
import json
import sys
from cache import Cache
from time import time

def retornaChaveValor(msg):
    return list(msg.keys())[0], list(msg.values())[0]

# inserir pedido
def inserePed(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    resp = enviarMsgReplica('r', chave)
    
    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Cliente "+ chave +" não autenticado"
        else:
            oid = time()
            cidOid = chave + ':' + str(int(oid))
            dict = { 'Produtos': {}, 'ValorTotal': 0 }
            resp = enviarMsgReplica('c', cidOid, dict)
            if resp['status'] == 'OK':
                return "Oid gerado: "+ str(int(oid))
            else:
                return str(resp['resposta'])
    else:
        return str(resp['resposta'])

# modificar pedido
def modPed(msg):
    msg = json.loads(msg)
    chave, valor = retornaChaveValor(msg) # Chave = CID:OID
    
    tmp = chave.split(':')
    cid = tmp[0]
    oid = tmp[1]
    resp = enviarMsgReplica('r', cid)

    # verifica erros e autentica
    if resp['status'] != 'OK':
        return str(resp['resposta'])
    if resp['resposta'] == 'None' or resp['resposta'] == None:
        return "Cliente "+ cid +" não autenticado" 

    resp2 = enviarMsgReplica('r', chave)

    # verifica erros e se pedido existe
    if resp2['status'] != 'OK':
        return str(resp['resposta'])
    if resp2['resposta'] == 'None' or resp2['resposta'] == None:
        return "Pedido com oid "+ oid +" não existe" 

    nomeP = valor['Produto']
    quantP = int(valor['Quantidade'])

    # verifica quantidade negativa
    if(quantP < 0):
        return "Quantidade invalida!"

    
    resp3 = enviarMsgReplica('r', nomeP)
    
    # verifica erros e se produto existe
    if resp3['status'] != 'OK':
        return str(resp['resposta'])
    if resp3['resposta'] == 'None' or resp3['resposta'] == None:
        return "Produto "+ nomeP + " não existe"

    ### modificação do pedido ###

    prodBD =   json.loads(resp3['resposta']) if type(resp3['resposta']) == str else resp3['resposta']
    quantBD = int(prodBD['Quantidade'])
    valorBD = int(prodBD['Valor'])
    quantBDTmp = quantBD
    
    pedido =  json.loads(resp2['resposta']) if type(resp2['resposta']) == str else resp2['resposta']
    produtos = pedido['Produtos']
    valorTotal = pedido['ValorTotal']
    produtoNoPedido = nomeP in produtos

    if quantP == 0:
        if not produtoNoPedido:
            return "Produto não está no pedido para ser retirado"
        else:
            quantBDTmp = quantBDTmp + int(produtos[nomeP])
            valorTotal = valorTotal - int(produtos[nomeP])*valorBD
            del produtos[nomeP]
    
    elif produtoNoPedido:
        diferenca = int(produtos[nomeP]) - quantP
        quantBDTmp = quantBDTmp + diferenca
        valorTotal = valorTotal - diferenca*valorBD
        produtos[nomeP] = quantP
        
    else:
        quantBDTmp = quantBDTmp - quantP
        valorTotal = valorTotal + quantP*valorBD
        produtos[nomeP] = quantP

    if quantBDTmp < 0:
        return "Quantidade insuficiente de produto "+nomeP+" para realizar pedido"
    
    # atualiza o pedido
    pedido['Produtos'] = produtos
    pedido['ValorTotal'] = valorTotal
    enviarMsgReplica('u', chave, pedido)

    if quantBDTmp != quantBD:
        # atualiza o produto
        prodBD['Quantidade'] = quantBDTmp
        enviarMsgReplica('u', nomeP, prodBD)

    return "Modificação realizada! Pedido: " + str(pedido) + "\nProduto: " + str(prodBD)

# enumerar pedido
def enumPed(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)

    tmp = chave.split(':')
    cid = tmp[0]
    oid = tmp[1]
    resp = enviarMsgReplica('r', chave) 

    if resp['status'] != 'OK':
        return str(resp['resposta'])
    if resp['resposta'] == 'None' or resp['resposta'] == None:
        return "Pedido com cid "+cid+" e oid "+oid+" não existe"

    pedido = json.loads(resp['resposta']) if type(resp['resposta']) == str else resp['resposta']
    produtos = pedido['Produtos']
    valorTotal = pedido['ValorTotal']

    return "Pedido encontrado! Produtos: " + str(produtos) + "\nValor total do pedido: " + str(valorTotal)

# Enumerar todos
def enumAll(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)
    chaveInterval = str(chave)+':0#'+str(chave)+':'+str(int(time()))

    resp = enviarMsgReplica('rm', chaveInterval)

    if resp['status'] != 'OK':
        return str(resp['resposta'])
    if resp['resposta'] == 'None' or resp['resposta'] == None:
        return "Não exitem pedidos para o cid " + chave

    pedidos = resp['resposta']

    retorno = "Pedidos encontrados: \n"
    for nomePedido in pedidos:
        oid = nomePedido.split(':')[1]
        retorno = retorno + oid +" -> "+ pedidos[nomePedido]+ "\n"

    return retorno

# excluir pedido
def exclPed(msg):
    msg = json.loads(msg)
    chave, _ = retornaChaveValor(msg)

    tmp = chave.split(':')
    cid = tmp[0]
    oid = tmp[1]
    resp = enviarMsgReplica('r', chave)

    if resp['status'] == 'OK':
        if resp['resposta'] == 'None' or resp['resposta'] == None:
            return "Pedido de oid "+ oid +" não encontrado"  
        else:
            pedido = json.loads(resp['resposta']) if type(resp['resposta']) == str else resp['resposta']
            produtos = pedido['Produtos']

            for nomeProduto in produtos:

                resp2 = enviarMsgReplica('r', nomeProduto)
                
                # verifica erros e se produto existe
                if resp2['status'] != 'OK':
                    return str(resp['resposta'])
                if resp2['resposta'] == 'None' or resp2['resposta'] == None:
                    return "Produto "+ nomeProduto + " não existe"
                
                # modifica quantidade do produto no banco
                prodBD = json.loads(resp2['resposta']) if type(resp2['resposta']) == str else resp2['resposta']
                quantBD = int(prodBD['Quantidade']) + int(produtos[nomeProduto])
                prodBD['Quantidade'] = quantBD

                resp3 = enviarMsgReplica('u', nomeProduto, prodBD)

                # verifica se atualizou a quantidade
                if resp3['status'] != 'OK':
                    return str(resp['resposta'])

            resp = enviarMsgReplica('d', chave)

            # verifica se apagou o pedido
            if resp['status'] != 'OK':
                return str(resp['resposta'])
            return "Pedido " + oid + " excluido"
    else:
        return str(resp['resposta'])
        
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

    global CliCache, SocketRepl

    # Se for read tenta acessar o cache
    if funcao == 'r':
        valorC = CliCache.ler(chave)
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
            CliCache.inserir(chave, valor)
            print('CACHE: Inserido', chave, valor)
        if funcao == 'r':
            CliCache.inserir(chave, respJson['resposta'])
            print('CACHE: Inserido', chave, respJson['resposta'])
        if funcao == 'u':
            CliCache.inserir(chave, valor)
            print('CACHE: Atualizado', chave, valor)
        if funcao == 'd':
            CliCache.inserir(chave, None)
            print('CACHE: Deletado', chave)

    return respJson

if __name__ == '__main__':      # Main

    # globais
    NumReplica = 0
    SocketRepl = None
    CliCache = Cache()

    # Conectar no socket das replicas
    escolheReplicaValida()

    # Conectar no socket adm/admPortal
    porta = int(input("Porta do socket cli-cliPortal (default 54321): "))
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
        # Conexão estabelecida
        status = 1
        c, addr = sPor.accept()
        data = c.recv(1024)
        msg = data.decode()

        # Inserir Pedido
        if msg[0] == "i":           
            status = inserePed(msg[2:])
            print(status)
            c.send(status.encode())

        # Modificar Pedido
        elif msg[0] == "m":
            status = modPed(msg[2:])
            print(status)
            c.send(status.encode())

        # Enumerar pedido por OID
        elif msg[0] == "e":
            status = enumPed(msg[2:])
            print(status)
            c.send(status.encode())
        
        # Enumera pedido do CID
        elif msg[0] == "E":
            status = enumAll(msg[2:])
            print(status)
            c.send(status.encode())
        
        # Exclui pedido
        elif msg[0] == "x":
            status = exclPed(msg[2:])
            print(status)
            c.send(status.encode())
        else:
            print('Operação falhada!')
            c.send('Operação falhada!'.encode())

        c.close()
