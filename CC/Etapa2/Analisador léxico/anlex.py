

from asyncio.windows_events import NULL
from re import X


def addtab(elem, tab):   # Função para inserir na tabela de simbolos
    nelem = 1
    tab.seek(0, 0)
    for linha in tab:
        if (str(elem+'\n')) == linha:
            return nelem
        if str(elem) == linha:
            return nelem
        nelem += 1

    tab.writelines(elem+"\n")
    return nelem


def buscar_token(arq, tk):  # Busacar token numero tk
    Tab_Simb = open("Tab_Simb.txt", "r+")
    NUM = ['0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9']  # Constante numerica
    LUpp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    LDnn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ProbID = ['a', 'g', 'h', 'j', 'k', 'l', 'm',
              'n', 'o', 'q', 'u', 'v', 'x', 'y', 'z', '_']
    IDS = ['_'] + LUpp + LDnn + NUM
    strSimb = ''
    ProbID.extend(LUpp)
    nlinha = 1  # numero da linha    .tell() mostra a posição do ponteiro
    ncoluna = 0  # numero da coluna  arq.seek(-1, 1) volta 1 casa
    lah = False   # Look Ahead - como o maximo é de 1 caractere, não é necessario voltar mais do que 1
    estado = 0  # Estado atual
    ntk = 1  # numero do token

    while 1:
        if lah == False:  # Look Ahead
            carac = arq.read(1)
            ncoluna += 1
        strSimb = strSimb + str(carac)
        lah = False
#################### Estado 0 ####################
        if estado == 0:
            if carac == ':':
                estado = 1

            elif carac == '^':  # Caractere ^
                if ntk == tk:
                    return ('^', 'EXP',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '/':  # Caractere /
                if ntk == tk:
                    return ('/', 'DIV',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '*':  # Caractere *
                if ntk == tk:
                    return ('*', 'MUL',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '-':  # Caractere -
                if ntk == tk:
                    return ('-', 'SUB',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '+':  # Caractere +
                if ntk == tk:
                    return ('+', 'ADD',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == ';':  # Caractere ;
                if ntk == tk:
                    return (';', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '(':  # Caractere (
                if ntk == tk:
                    return ('(', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == ')':  # Caractere )
                if ntk == tk:
                    return (')', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif (carac == ' ') | (carac == '\n') | (carac == '\t'):  # Caractere de ws
                if carac == '\n':
                    nlinha = nlinha + 1
                    ncoluna = 0
                estado = 12

            elif carac == '[':  # Caractere de comentário
                estado = 14

            elif carac == '~':  # Caractere de relop NE
                estado = 16

            elif carac == '=':  # Caractere de relop EQ
                if ntk == tk:
                    return ('RELOP', 'EQ',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0

            elif carac == '<':  # Caractere de relop LT ou LE
                estado = 19

            elif carac == '>':  # Caractere de relop GE ou GT
                estado = 22

            elif carac in NUM:  # Caractere  num
                estado = 27

            elif carac == 'p':  # Caractere  p
                estado = 36

            elif carac == 'r':  # Caractere  r
                estado = 45

            elif carac == 'w':  # Caractere  w
                estado = 52

            elif carac == 'b':  # Caractere  b
                estado = 58

            elif carac == 'f':  # Caractere  f
                estado = 64

            elif carac == 'd':  # Caractere  d
                estado = 70

            elif carac == 't':  # Caractere  t
                estado = 73

            elif carac == 'c':  # Caractere  c
                estado = 78

            elif carac == 'e':  # Caractere  e
                estado = 83

            elif carac == 'i':  # Caractere  i
                estado = 91

            elif carac in ProbID:  # Caractere  do ID
                estado = 25

            else:  # Erro
                if not carac:   # eof
                    break
                return ('ERRO', 'ERRO', (nlinha, ncoluna))

#################### Estado 1 ####################
        elif estado == 1:
            if carac == '=':    # caractere :=
                if ntk == tk:
                    return (':=', 'ATR',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
            else:   # caractere =
                if ntk == tk:
                    return (':', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 12 ####################
        elif estado == 12:
            # Caractere de ws WS não retorna nada!
            if (carac == ' ') | (carac == '\n') | (carac == '\t'):
                if carac == '\n':
                    nlinha = nlinha + 1
                    ncoluna = 0
                estado = 12
            else:
                # if ntk == tk:
                #    return ('ws', NULL,  (nlinha, ncoluna))
                # else:
                #    ntk += 1
                strSimb = ''
                estado = 0
                lah = True

#################### Estado 14 ####################
        elif estado == 14:  # Comentario não retorna nada
            if carac != ']':
                estado = 14
            else:
                # if ntk == tk:
                #    return ('Coment', NULL,  (nlinha, ncoluna))
                # else:
                #    ntk += 1
                strSimb = ''
                estado = 0

#################### Estado 16 ####################
        elif estado == 16:  # Relop NE
            if carac == '=':
                if ntk == tk:
                    return ('RELOP', 'NE',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
            else:
                return ('ERRO', 'ERRO', (nlinha, ncoluna))

#################### Estado 19 ####################
        elif estado == 19:
            if carac == '=':  # Relop LE
                if ntk == tk:
                    return ('RELOP', 'LE',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
            else:           # Relop LT
                if ntk == tk:
                    return ('RELOP', 'LT',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 22 ####################
        elif estado == 22:
            if carac == '=':  # Relop GE
                if ntk == tk:
                    return ('RELOP', 'GE',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
            else:           # Relop GT
                if ntk == tk:
                    return ('RELOP', 'GT',  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 27 ####################
        elif estado == 27:
            if carac in NUM:  # Num
                estado = 27
            elif carac == '.':  # Num Frac
                estado = 29
            elif carac == 'E':  # Num Exp
                estado = 32
            else:
                if ntk == tk:
                    x = addtab(strSimb[:-1], Tab_Simb)
                    return ('setInt', x,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 29 ####################
        elif estado == 29:
            if carac in NUM:  # Num
                estado = 30
            else:
                return ('ERRO', 'ERRO', (nlinha, ncoluna))

#################### Estado 30 ####################
        elif estado == 30:
            if carac in NUM:  # Num Frac
                estado = 30
            elif carac == 'E':  # Num Exp
                estado = 32
            else:
                if ntk == tk:
                    x = addtab(strSimb[:-1], Tab_Simb)
                    return ('setFrac', x,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 32 ####################
        elif estado == 32:
            if (carac == '+') | (carac == '-'):  # Num Exp
                estado = 33
            elif carac in NUM:
                estado = 34
            else:
                return ('ERRO', 'ERRO', (nlinha, ncoluna))

#################### Estado 33 ####################
        elif estado == 33:
            if carac in NUM:  # Num
                estado = 34
            else:
                return ('ERRO', 'ERRO', (nlinha, ncoluna))

#################### Estado 34 ####################
        elif estado == 34:
            if carac in NUM:  # Num EXP
                estado = 34
            else:
                if ntk == tk:
                    x = addtab(strSimb[:-1], Tab_Simb)
                    return ('setExp', x,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 36 até 43 - programa
#################### Estado 36 ####################
        elif estado == 36:
            if carac == 'r':    # caractere r
                estado = 37
            else:
                estado = 25     # id

#################### Estado 37 ####################
        elif estado == 37:
            if carac == 'o':    # caractere o
                estado = 38
            else:
                estado = 25     # id

#################### Estado 38 ####################
        elif estado == 38:
            if carac == 'g':    # caractere g
                estado = 39
            else:
                estado = 25     # id

#################### Estado 39 ####################
        elif estado == 39:
            if carac == 'r':    # caractere r
                estado = 40
            else:
                estado = 25     # id

#################### Estado 40 ####################
        elif estado == 40:
            if carac == 'a':    # caractere a
                estado = 41
            else:
                estado = 25     # id

#################### Estado 41 ####################
        elif estado == 41:
            if carac == 'm':    # caractere m
                estado = 42
            else:
                estado = 25     # id

#################### Estado 42 ####################
        elif estado == 42:
            if carac == 'a':    # caractere a
                estado = 43
            else:
                estado = 25     # id

#################### Estado 43 ####################
        elif estado == 43:
            if carac in IDS:    # IDS
                estado = 25
            else:  # [^IDS]
                if ntk == tk:
                    return ('programa', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 45 até 50 - repeat
#################### Estado 45 ####################
        elif estado == 45:
            if carac == 'e':    # caractere e
                estado = 46
            else:
                estado = 25     # id

#################### Estado 46 ####################
        elif estado == 46:
            if carac == 'p':    # caractere p
                estado = 47
            else:
                estado = 25     # id

#################### Estado 47 ####################
        elif estado == 47:
            if carac == 'e':    # caractere e
                estado = 48
            else:
                estado = 25     # id

#################### Estado 48 ####################
        elif estado == 48:
            if carac == 'a':    # caractere a
                estado = 49
            else:
                estado = 25     # id

#################### Estado 49 ####################
        elif estado == 49:
            if carac == 't':    # caractere t
                estado = 50
            else:
                estado = 25     # id

#################### Estado 50 ####################
        elif estado == 50:
            if carac in IDS:    # caractere a
                estado = 25
            else:
                if ntk == tk:
                    return ('repeat', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 52 até 56 - while
#################### Estado 52 ####################
        elif estado == 52:
            if carac == 'h':    # caractere h
                estado = 53
            else:
                estado = 25     # id

#################### Estado 53 ####################
        elif estado == 53:
            if carac == 'i':    # caractere i
                estado = 54
            else:
                estado = 25     # id

#################### Estado 54 ####################
        elif estado == 54:
            if carac == 'l':    # caractere l
                estado = 55
            else:
                estado = 25     # id

#################### Estado 55 ####################
        elif estado == 55:
            if carac == 'e':    # caractere e
                estado = 56
            else:
                estado = 25     # id

#################### Estado 56 ####################
        elif estado == 56:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('while', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 58 até 62 - begin
#################### Estado 58 ####################
        elif estado == 58:
            if carac == 'e':    # caractere e
                estado = 59
            else:
                estado = 25     # id

#################### Estado 59 ####################
        elif estado == 59:
            if carac == 'g':    # caractere g
                estado = 60
            else:
                estado = 25     # id

#################### Estado 60 ####################
        elif estado == 60:
            if carac == 'i':    # caractere i
                estado = 61
            else:
                estado = 25     # id

#################### Estado 61 ####################
        elif estado == 61:
            if carac == 'n':    # caractere n
                estado = 62
            else:
                estado = 25     # id

#################### Estado 62 ####################
        elif estado == 62:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('begin', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 64 até 68 - float
#################### Estado 64 ####################
        elif estado == 64:
            if carac == 'l':    # caractere l
                estado = 65
            else:
                estado = 25     # id

#################### Estado 65 ####################
        elif estado == 65:
            if carac == 'o':    # caractere o
                estado = 66
            else:
                estado = 25     # id

#################### Estado 66 ####################
        elif estado == 66:
            if carac == 'a':    # caractere a
                estado = 67
            else:
                estado = 25     # id

#################### Estado 67 ####################
        elif estado == 67:
            if carac == 't':    # caractere t
                estado = 68
            else:
                estado = 25     # id

#################### Estado 68 ####################
        elif estado == 68:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('float', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 70 até 71 - do
#################### Estado 70 ####################
        elif estado == 70:
            if carac == 'o':    # caractere o
                estado = 71
            else:
                estado = 25     # id

#################### Estado 71 ####################
        elif estado == 71:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('do', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 73 até 76 - then
#################### Estado 73 ####################
        elif estado == 73:
            if carac == 'h':    # caractere h
                estado = 74
            else:
                estado = 25     # id

#################### Estado 74 ####################
        elif estado == 74:
            if carac == 'e':    # caractere e
                estado = 75
            else:
                estado = 25     # id

#################### Estado 75 ####################
        elif estado == 75:
            if carac == 'n':    # caractere n
                estado = 76
            else:
                estado = 25     # id

#################### Estado 76 ####################
        elif estado == 76:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('then', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 78 até 81 - char
#################### Estado 78 ####################
        elif estado == 78:
            if carac == 'h':    # caractere h
                estado = 79
            else:
                estado = 25     # id

#################### Estado 79 ####################
        elif estado == 79:
            if carac == 'a':    # caractere a
                estado = 80
            else:
                estado = 25     # id

#################### Estado 80 ####################
        elif estado == 80:
            if carac == 'r':    # caractere r
                estado = 81
            else:
                estado = 25     # id

#################### Estado 81 ####################
        elif estado == 81:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('char', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 83 até 86 - else
#################### Estado 83 ####################
        elif estado == 83:
            if carac == 'l':    # caractere l
                estado = 84
            elif carac == 'n':    # caractere n (end)
                estado = 88
            else:
                estado = 25     # id

#################### Estado 84 ####################
        elif estado == 84:
            if carac == 's':    # caractere s
                estado = 85
            else:
                estado = 25     # id

#################### Estado 85 ####################
        elif estado == 85:
            if carac == 'e':    # caractere e
                estado = 86
            else:
                estado = 25     # id

#################### Estado 86 ####################
        elif estado == 86:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('else', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 88 até 89 - end
#################### Estado 88 ####################
        elif estado == 88:
            if carac == 'd':    # caractere d
                estado = 89
            else:
                estado = 25     # id

#################### Estado 89 ####################
        elif estado == 89:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('end', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 91 até 92 - if
#################### Estado 91 ####################
        elif estado == 91:
            if carac == 'f':    # caractere f
                estado = 92
            elif carac == 'n':    # caractere n (int)
                estado = 94
            else:
                estado = 25     # id

#################### Estado 92 ####################
        elif estado == 92:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('if', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

# - 94 até 95 - int
#################### Estado 94 ####################
        elif estado == 94:
            if carac == 't':    # caractere t
                estado = 95
            else:
                estado = 25     # id

#################### Estado 95 ####################
        elif estado == 95:
            if carac in IDS:    # IDS
                estado = 25
            else:               # [^IDS]
                if ntk == tk:
                    return ('int', NULL,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

#################### Estado 25 ####################
        elif estado == 25:
            if carac in IDS:
                estado = 25
            else:
                if ntk == tk:
                    x = addtab(strSimb[:-1], Tab_Simb)
                    return ('ID', x,  (nlinha, ncoluna))
                else:
                    ntk += 1
                    strSimb = ''
                    estado = 0
                    lah = True

    return ('EOF', 'ERRO',  (nlinha, ncoluna))
