import eel
import json
import time
from mt import processamento_mt

#### Autores ####

# Arthur Labaki - 11821BCC017
# Vinicius Calixto - 11911BCC039
# Vinnicius Pereira - 11821BCC046

#### Machine call ####
# Octupla M=(Q,Σ,B,Γ1,Γ2,δ,q0,F)
# Transições: δ:Q×Γ1×Γ2 → Q×Γ1×Γ2×D1×D2
# Esquerda (E ou L) Direita (R ou D) Parado (P ou I)
#
#Ex1: A^nBA^n
#Ex2: ordenaçaâ de w = {A,B,C}*
#Ex3: WW^rW
#Ex4: 0^n1^n

# rpc call with frontend
def getMTJson(file_name, cad1, cad2):

    with open(file_name, 'r') as j:
        Ex = json.load(j)

    # Octupla de entrada
    est = Ex["estados"]
    alfa = Ex["alfabeto"]
    branco = Ex["branco"]
    alfa_f1 = Ex["alfabeto_fita1"]
    alfa_f2 = Ex["alfabeto_fita2"]
    transi = Ex["transicoes"]
    est_ini = Ex["estado_inicial"]
    est_fina = Ex["estados_finais"]

    processamento_mt(est, alfa, branco, alfa_f1, alfa_f2, transi, est_ini, est_fina, cad1, cad2)

    file = open("Ex-process.json", "r")
    data = file.read().rstrip()
    json_object = json.loads(data)
    return json_object

#### starts server ####
eel.init("web")

@eel.expose
def getPythonMTJson(cadeia1, cadeia2):
    
    start = time.time()
    x = getMTJson('Ex4.json', cadeia1, cadeia2)  # Cadeia de entrada
    end = time.time()
    
    x['timestamp'] = round(end-start, 5)
    return x

eel.start("main.html", host="localhost", port=8000, size=(1920,1080))