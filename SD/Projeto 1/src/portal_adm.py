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


def buscaCli(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return json.dumps(retornaValor(msg.keys()))
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


def buscaPro(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return json.dumps(retornaValor(msg.keys()))
    return 1


def inserePed(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        return 1
    cache.update(msg)
    return 0


def modificaPed(msg):
    global cache
    msg = json.loads(msg)
    if verificaCacheID(msg.keys()) == 1:
        cache.update(msg)
        return 0
    return 1


def excluiPed(msg):
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
            status = inserePed(msg[2:])
        if msg[0] == "m":
            status = modificaPed(msg[2:])
        if msg[0] == "e":
            status = excluiPed(msg[2:])
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
        print("Mensagem enviada")
    else:
        print("Mensagem não enviada, tente novamente\n")


if __name__ == '__main__':
    porta = int(input("Porta (default 12345): "))
    cache = {}

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
        status = 1  # supoe erro
        c, addr = s.accept()
        data = c.recv(1024)
        msg = data.decode()

        if msg[1] == "c":
            if msg[0] == "i":   # Inserir Cliente
                status = insereCli(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Insercao de cliente realizada!'.encode())

            elif msg[0] == "m":  # Modificar Cliente
                status = modificaCli(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Modificacao de cliente realizada!'.encode())

            elif msg[0] == "e":  # Excluir Cliente
                status = excluiCli(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Exclucao de cliente realizada!'.encode())

            elif msg[0] == "b":  # Buscar Cliente
                status = buscaCli(msg[2:])
                if status != 1:
                    envio = 'Busca de cliente realizada!\n' + status
                    c.send(envio.encode())
                else:
                    c.send('Cliente nao existe!'.encode())
            else:
                c.send('Operação falhada!'.encode())

        elif msg[1] == "p":
            if msg[0] == "i":   # Inserir Produto
                status = inserePro(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Insercao de produto realizada!'.encode())

            elif msg[0] == "m":  # Modificar Produto
                status = modificaPro(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Modificacao de produto realizada!'.encode())

            elif msg[0] == "e":  # Excluir Produto
                status = excluiPro(msg[2:])
                if status == 0:
                    publish(client, msg)
                    c.send('Exclusao de produto realizada!'.encode())

            elif msg[0] == "b":  # Buscar Produto
                status = buscaPro(msg[2:])
                if status != 1:
                    envio = 'Busca de produto realizada!\n' + status
                    c.send(envio.encode())
                else:
                    c.send('Produto nao existe!'.encode())
            else:
                c.send('Operação falhada!'.encode())
        else:
            c.send('Operação falhada!'.encode())

        c.close()
