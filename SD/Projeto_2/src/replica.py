import plyvel
from pysyncobj import SyncObj, replicated
import socket

import sys
import threading
import json

class ControleReplica():

    def __init__(self, numReplica):

        if numReplica == 0:
            self.portaSocket = 6010
            self.replica = Replica(self.portaSocket, 'localhost:6000', ['localhost:6001', 'localhost:6002'])
        elif numReplica == 1:
            self.portaSocket = 6011
            self.replica = Replica(self.portaSocket, 'localhost:6001', ['localhost:6000', 'localhost:6002'])
        else:
            self.portaSocket = 6012
            self.replica = Replica(self.portaSocket, 'localhost:6002', ['localhost:6000', 'localhost:6001'])
    
    # conexão thread socket com portal
    def iniciarSocket(self):

        s = socket.socket()
        host = socket.gethostname()
        s.bind((host, self.portaSocket))
        s.listen(20)

        print('Host socket da replica de porta ' + str(self.portaSocket) + ' disponivel')
        print('Replica pronta para uso')

        while True:
            con, end = s.accept()
            print('Conexao com ' + str(end) + ' estabelecida')
            threading.Thread(target=self.controleReplica, args=(con, end)).start()

    # Fluxo principal de controle da replica
    def controleReplica(self, con, end):

        msg = None

        while True:
            data = con.recv(10240)
            msg = data.decode()
            if msg:
                
                jsonResp = json.loads(msg)
                funcao = jsonResp['funcao']
                chave = jsonResp['chave']
                valor = str(jsonResp['valor'])

                if(funcao == 'c'):
                    try:
                        self.replica.escrever(chave, valor)
                        resp = json.dumps({'status': 'OK', 'resposta': 'Escrito' })
                    except BaseException as e:
                        resp = json.dumps({'status': 'ERROR', 'resposta': str(e) })
                
                elif(funcao == 'r'):
                    try:
                        statusBD, respBD = self.replica.ler(chave)
                        resp = json.dumps({'status': statusBD, 'resposta': respBD })
                    except BaseException as e:
                        resp = json.dumps({'status': 'ERROR', 'resposta': str(e) })
                
                elif(funcao == 'rm'):
                    try:
                        tmp = chave.split('#')
                        chaveInicial = tmp[0]
                        chaveFinal = tmp[1]
                        statusBD, respBD = self.replica.lerMuitos(chaveInicial, chaveFinal)
                        resp = json.dumps({'status': statusBD, 'resposta': respBD })
                    except BaseException as e:
                        resp = json.dumps({'status': 'ERROR', 'resposta': str(e) })
                
                elif(funcao == 'u'):
                    try:
                        self.replica.apagar(chave)
                        self.replica.escrever(chave, valor)
                        resp = json.dumps({'status': 'OK', 'resposta': 'Atualizado' })
                    except BaseException as e:
                        resp = json.dumps({'status': 'ERROR', 'resposta': str(e) })


                elif(funcao == 'd'):
                    try:
                        self.replica.apagar(chave)
                        resp = json.dumps({'status': 'OK', 'resposta': 'Apagado' })
                    except BaseException as e:
                        resp = json.dumps({'status': 'ERROR', 'resposta': str(e) })
                
                else:
                    resp = json.dumps({'status': 'ERRO', 'resposta': 'String crud errada ' + str(funcao) })
                
                msg = None
                con.send(resp.encode())
        
class Replica(SyncObj):

    def __init__(self, port, lider, parceiras):
        super(Replica, self).__init__(lider, parceiras)
        self.nomeDB = './database/' + str(port) + '/'

    @replicated
    def escrever(self, chave, valor):

        try:

            baseDados = plyvel.DB(self.nomeDB, create_if_missing=True)

            chaveBytes = bytes(chave, 'utf-8')
            valorBytes = bytes(valor,'utf-8')
            baseDados.put(chaveBytes, valorBytes)
            print('create', self.nomeDB, chave, valor, json.dumps({'status': 'OK', 'resposta': 'Escrito' }))

            baseDados.close()

        except BaseException as e:
            print('ERROR!!!', 'create', self.nomeDB, chave, valor, json.dumps({'status': 'ERROR', 'resposta': str(e) }))
        
    def ler(self, chave):
        
        try:

            baseDados = plyvel.DB(self.nomeDB, create_if_missing=True)

            chaveBytes = bytes(chave, 'utf-8')
            respBytes = baseDados.get(chaveBytes)
            resp = None if not respBytes else respBytes.decode()
            print('read', self.nomeDB, chave, json.dumps({'status': 'OK', 'resposta': resp }))
            
            baseDados.close()
            return 'OK', resp

        except BaseException as e:
            return 'ERROR', str(e)
    
    def lerMuitos(self, chaveInicial, chaveFinal):
        
        try:

            baseDados = plyvel.DB(self.nomeDB, create_if_missing=True)

            chaveIniBytes = bytes(chaveInicial, 'utf-8')
            chaveFinBytes = bytes(chaveFinal, 'utf-8')

            resp = {}
            for key, value in baseDados.iterator(start=chaveIniBytes, stop=chaveFinBytes):
                resp[key.decode()] = value.decode()
            print('read many', self.nomeDB, chaveInicial, chaveFinal, json.dumps({'status': 'OK', 'resposta': len(resp) }))
            
            baseDados.close()
            resp == json.dumps(resp) if resp != {} else None
            return 'OK', resp

        except BaseException as e:
            return 'ERROR', str(e)
    
    @replicated
    def apagar(self, chave):

        try:

            baseDados = plyvel.DB(self.nomeDB, create_if_missing=True)

            chaveBytes = bytes(chave, 'utf-8')
            baseDados.delete(chaveBytes)
            print('delete', self.nomeDB, chave, json.dumps({'status': 'OK', 'resposta': 'Apagado' }))

            baseDados.close()

        except BaseException as e:
            print('ERROR!!!', 'delete', self.nomeDB, chave, json.dumps({'status': 'ERROR', 'resposta': str(e) }))

if __name__ == "__main__":

    if sys.argv and sys.argv[1] and sys.argv[1].isnumeric():
        numReplica = int(sys.argv[1])
        
        if numReplica < 0 or numReplica > 2:
            print("Falha ao iniciar a replica " + str(numReplica) + ". O número da replica deve estar no intervalo inteiro [0,2]")
        
        else:
            print('Iniciando a replica ' + str(numReplica) + ' ...')
            replica = ControleReplica(numReplica)

            print('Conectando socket do portal e replica ...')
            replica.iniciarSocket()
    
    else:
        print("Falha ao iniciar a replica, deve ser passado um argumento com o numero da replica no intervalo [0,2]")
    
    input("Pressione algo para finalizar...")