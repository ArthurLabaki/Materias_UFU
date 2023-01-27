import socket
import json
import random
from paho.mqtt import client as mqtt_client
import threading
import sys


def verificaCacheID(ID):
    global cache
    [ID] = list(ID)
    for elem in list(cache.keys()):
        if elem == ID:
            return 1  # 1 = existe
    return 0  # 0 = não existe


def retornaValor(ID):
    global cache
    [ID] = list(ID)
    for elem in list(cache.keys()):
        if elem == ID:
            return cache[elem]  # retorna valores


def retornaLista(ID):
    global cache
    [ID] = list(ID)
    ID = ID+':'
    lst = []
    for elem in list(cache.keys()):
        if ID in elem:
            lst.append(elem)
    if len(lst) == 0:
        return 1
    else:
        return lst


def insereCli(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:  # Checa se existe
        return 1
    cache.update(msg)
    return 0


def modificaCli(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        cache.update(msg)
        return 0
    return 1


def excluiCli(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [elem] = list(msg.keys())
        cache.pop(elem)
        return 0
    return 1


def inserePro(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return 1
    cache.update(msg)
    return 0


def modificaPro(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        cache.update(msg)
        return 0
    return 1


def excluiPro(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [elem] = list(msg.keys())
        cache.pop(elem)
        return 0
    return 1


def inserePed(msg, id):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [chave] = list(msg.keys())
        txt = chave + ':' + str(id)
        dict = {txt: {}}
        if verificaCacheID(dict.keys()) == 1:
            return 1
        else:
            cache.update(dict)
            ret = json.dumps(dict)
            return ret
    return 1


def retornaProd(prod):
    global cache
    for elem in list(cache.keys()):
        if prod == elem:
            return cache[prod]


def modPed(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [ID] = list(msg.keys())  # ID = string
        [dict] = list(msg.values())
        prd = dict['Produto']
        qnt = int(dict['Quantidade'])
        if qnt <= 0:  # Quantidade insuficiente
            return [1]
        produto = retornaProd(prd)
        if produto == None:
            return [1]
        quantprod = int(produto['Quantidade'])
        valprod = int(produto['Valor'])
        if quantprod < qnt:  # Não existe produto ou não tem suficiente
            return [1]
        novaquant = quantprod - qnt
        produto.update({'Quantidade': novaquant})
        valprod = valprod * qnt
        pedido = {ID: {'Produto': prd, 'Quantidade': qnt, 'Preco': valprod}}
        novoprod = {prd: produto}
        cache.update(pedido)
        return [pedido, novoprod]
    return [1]


def enumPed(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return json.dumps(retornaValor(msg.keys()))
    return 1


def enumAll(msg):
    global cache
    msg = json.loads(msg)
    val = 0
    ped = []
    if verificaCacheID(msg.keys()) == 1:
        lst = retornaLista(msg.keys())
        for i in lst:
            elem = retornaProd(i)
            val = val + float(elem['Preco'])
            ped.append({i: elem})
        return [ped, val]
    return [1]


def exclPed(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [ID] = list(msg.keys())  # ID = string
        [dict] = list(msg.values())
        if dict == {}:
            cache.pop(ID)
            return [ID, {ID: 0}]
        prd = dict['Produto']
        qnt = int(dict['Quantidade'])
        produto = retornaProd(prd)
        quantprod = int(produto['Quantidade'])
        novaquant = quantprod + qnt
        produto.update({'Quantidade': novaquant})
        novoprod = {prd: produto}
        cache.pop(ID)
        return [ID, {ID: 0}, novoprod]
    return [1]


def inserePed1(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return 1
    cache.update(msg)
    return 0


def modificaPed1(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        cache.update(msg)
        return 0
    return 1


def excluiPed1(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        [elem] = list(msg.keys())
        cache.pop(elem)
        return 0
    return 1


def pubsub(client):
    client.loop_start()


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao barramento MQTT")
        else:
            print("Falha ao conectar ao barramento MQTT, erro:", rc)
    try:
        client = mqtt_client.Client(client_id)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
    except:
        print('Falha ao conectar ao barramento MQTT \nFinalizando programa!')
        sys.exit()

    return client


def atualizaCache(msg):
    global cache
    if msg[1] == "c":
        if msg[0] == "i":
            status = insereCli(msg[2:])
        if msg[0] == "m":
            status = modificaCli(msg[2:])
        if msg[0] == "e":
            status = excluiCli(msg[2:])
    elif msg[1] == "p":
        if msg[0] == "i":
            status = inserePro(msg[2:])
        if msg[0] == "m":
            status = modificaPro(msg[2:])
        if msg[0] == "e":
            status = excluiPro(msg[2:])
    elif msg[1] == "r":
        if msg[0] == "i":
            status = inserePed1(msg[2:])
        if msg[0] == "m":
            status = modificaPed1(msg[2:])
        if msg[0] == "e":
            status = excluiPed1(msg[2:])
    print(cache, "\n")


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        atualizaCache(msg.payload.decode())
    try:
        client.subscribe(topic)
        client.on_message = on_message
    except:
        print('Falha ao se increver no topico do barramento MQTT \nFinalizando programa!')
        sys.exit()


def publish(client, msg):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print("Mensagem enviada\n")
    else:
        print("Mensagem não enviada, tente novamente\n")


if __name__ == '__main__':      # Main
    porta = int(input("Porta (default 54321): "))
    cache = {}
    id = 0

    # Conectar ao pub/sub por thread
    broker = 'broker.emqx.io'
    port = 1883
    topic = "sd-trab/projeto1"
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    username = 'emqx'
    password = 'public'
    client = connect_mqtt()
    subscribe(client)
    threading.Thread(target=pubsub(client)).start()

    # Conectar no socket
    try:
        s = socket.socket()
        host = socket.gethostname()
        s.bind((host, porta))
    except:
        print('Falha ao se conectar ao socket \nFinalizando programa!')
        sys.exit()

    s.listen(5)
    while True:
        # Conexão estabelecida
        status = 1  # supoe erro
        c, addr = s.accept()
        data = c.recv(1024)
        msg = data.decode()

        if msg[0] == "i":           # Inserir Pedido
            status = inserePed(msg[2:], id)
            if status != 1:
                ret = 'Pedido criado!\nOID: ' + str(id)
                status = 'ir'+status
                id = id + 1
                c.send(ret.encode())
                publish(client, status)
            else:
                c.send('Cliente não autenticado'.encode())

        elif msg[0] == "m":         # Modificar Pedido
            status = modPed(msg[2:])
            if status[0] != 1:
                msg1 = 'mr'+json.dumps(status[0])
                publish(client, msg1)
                msg2 = 'mp'+json.dumps(status[1])
                publish(client, msg2)
                c.send('Modificacao de pedido realizada!'.encode())
            else:
                c.send('Modificação não realizada'.encode())

        elif msg[0] == "e":         # Enumera pedido por OID
            status = enumPed(msg[2:])
            if status != 1:
                ret = 'Pedido encontrado!\n' + status
                c.send(ret.encode())
            else:
                c.send('Enumeração não realizada'.encode())

        elif msg[0] == "E":         # Enumera pedido do CID
            status = enumAll(msg[2:])
            if status[0] != 1:
                ret = 'Pedidos encontrados!\n' + \
                    str(status[0]) + '\nValor Total: ' + str(status[1])
                c.send(ret.encode())
            else:
                c.send('Enumeração não realizada'.encode())

        elif msg[0] == "x":         # Exclui pedido
            status = exclPed(msg[2:])
            if status[0] != 1:
                ret = 'Pedido de OID:' + str(status[0]) + ' removido'
                c.send(ret.encode())
                if len(status) == 2:
                    msg1 = 'er'+json.dumps(status[1])
                    publish(client, msg1)
                else:
                    msg1 = 'er'+json.dumps(status[1])
                    publish(client, msg1)
                    msg2 = 'mp'+json.dumps(status[2])
                    publish(client, msg2)
            else:
                c.send('Exclusao não realizada'.encode())
        else:
            c.send('Operação falhada!'.encode())

        c.close()
