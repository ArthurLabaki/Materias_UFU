import eel
import json
from mt import mt_process

#### Machine call ####
# Setupla M=(Q,Σ,Γ,δ,q0,B,F)
# Transições: δ:Q×Γ→Q×Γ×D
# Esquerda (E ou L) Direita (R ou D)

def getMTJson(file_name, cad):

    with open(file_name, 'r') as j:
        Ex = json.load(j)

    est = Ex["estados"]
    alfa = Ex["alfabeto"]
    alfa_f = Ex["alfabeto_fita"]
    transi = Ex["transicoes"]
    est_ini = Ex["estado_inicial"]
    branco = Ex["branco"]
    est_fini = Ex["estados_finais"]

    mt_process(est, alfa, alfa_f, transi, est_ini, branco, est_fini, cad)

    file = open("Ex-process.json", "r")
    data = file.read().rstrip()
    json_object = json.loads(data)
    return json_object

#### starts server ####
eel.init("web")

@eel.expose
def getPythonMTJson():
    x = getMTJson('Ex3.json', 'aaaabbbbcccc')
    return x

eel.start("main.html", host="localhost", port=8080, size=(1280,720))