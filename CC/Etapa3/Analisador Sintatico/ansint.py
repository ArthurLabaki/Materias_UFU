from anlex import *


def lex(token):  # Busca proximo lexema
    (nome, atr, (linha, coluna)) = buscar_token(arq, token)
    global i
    i += 1
    arq.seek(0, 0)
    if atr == NULL:
        atr = '-'
    if nome == 'ERRO':
        print(
            f"Erro no caractere {atr} \nEncontrado na linha {linha} e coluna {coluna}")
        exit()
    if nome == 'EOF':
        return (nome, 'EOF', (linha, coluna))
    return (nome, atr, (linha, coluna))


def erro(proxToken, str):
    print("Erro encontrado!")
    print(
        f"Token '{str}' esperado, mas foi encontrado um '{proxToken[0]} {proxToken[1]}'")
    print(f"Linha {proxToken[2][0]} e coluna {proxToken[2][1]}")
    exit()


def Procedimento_EP():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'programa':
        proxToken = lex(i)
        pilha.append("programa")
        if proxToken[0] == 'ID':
            proxToken = lex(i)
            pilha.append("ID")
            pilha.append("Bloco")
            Procedimento_Bloco()
        else:
            erro(proxToken, "ID")
    else:
        erro(proxToken, "programa")
    return 0


def Procedimento_Bloco():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'begin':
        proxToken = lex(i)
        pilha.append("begin")
        pilha.append("DVar")
        Procedimento_DVar()
        pilha.append("SCom")
        Procedimento_SCom()
        if proxToken[0] == 'end':
            proxToken = lex(i)
            pilha.append("end")
        else:
            erro(proxToken, "end")
    else:
        erro(proxToken, "begin")

    return 0


def Procedimento_DVar():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'tipo':
        pilha.append("Var")
        Procedimento_Var()
        pilha.append("DVar")
        Procedimento_DVar()
    return 0


def Procedimento_SCom():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if (proxToken[0] == 'if') | (proxToken[0] == 'ID') | (proxToken[0] == 'while') | (proxToken[0] == 'repeat') | (proxToken[0] == 'num') | (proxToken[0] == '('):
        pilha.append("Com")
        Procedimento_Com()
        pilha.append("SCom")
        Procedimento_SCom()
    return 0


def Procedimento_Var():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'tipo':
        proxToken = lex(i)
        pilha.append("tipo")
        if proxToken[0] == ':':
            proxToken = lex(i)
            pilha.append(":")
            if proxToken[0] == 'ID':
                pilha.append("ID")
                proxToken = lex(i)
                pilha.append("IDs")
                Procedimento_IDs()
                if proxToken[0] == ';':
                    pilha.append(";")
                    proxToken = lex(i)
                else:
                    erro(proxToken, ";")
            else:
                erro(proxToken, "ID")
        else:
            erro(proxToken, ":")
    else:
        erro(proxToken, "tipo")
    return 0


def Procedimento_IDs():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == ',':
        proxToken = lex(i)
        pilha.append(",")
        if proxToken[0] == 'ID':
            proxToken = lex(i)
            pilha.append("ID")
            pilha.append("IDs")
            Procedimento_IDs()
        else:
            erro(proxToken, "ID")
    else:
        return 0


def Procedimento_Com():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'if':
        proxToken = lex(i)
        pilha.append("if")
        if proxToken[0] == '(':
            proxToken = lex(i)
            pilha.append("(")
            pilha.append("Cond")
            Procedimento_Cond()
            if proxToken[0] == ')':
                proxToken = lex(i)
                pilha.append(")")
                if proxToken[0] == 'then':
                    proxToken = lex(i)
                    pilha.append("then")
                    pilha.append("Bloco")
                    Procedimento_Bloco()
                    if proxToken[0] == 'else':
                        proxToken = lex(i)
                        pilha.append("else")
                        pilha.append("Bloco")
                        Procedimento_Bloco()
                    else:
                        erro(proxToken, "else")
                else:
                    erro(proxToken, "then")
            else:
                erro(proxToken, ")")
        else:
            erro(proxToken, "(")

    elif proxToken[0] == 'while':
        proxToken = lex(i)
        pilha.append("while")
        if proxToken[0] == '(':
            proxToken = lex(i)
            pilha.append("(")
            pilha.append("Cond")
            Procedimento_Cond()
            if proxToken[0] == ')':
                proxToken = lex(i)
                pilha.append(")")
                if proxToken[0] == 'do':
                    proxToken = lex(i)
                    pilha.append("do")
                    pilha.append("Bloco")
                    Procedimento_Bloco()
                else:
                    erro(proxToken, "do")
            else:
                erro(proxToken, ")")
        else:
            erro(proxToken, "(")

    elif proxToken[0] == 'repeat':
        proxToken = lex(i)
        pilha.append("repeat")
        pilha.append("Bloco")
        Procedimento_Bloco()
        if proxToken[0] == 'while':
            proxToken = lex(i)
            pilha.append("while")
            if proxToken[0] == '(':
                proxToken = lex(i)
                pilha.append("(")
                pilha.append("Cond")
                Procedimento_Cond()
                if proxToken[0] == ')':
                    proxToken = lex(i)
                    pilha.append(")")
                else:
                    erro(proxToken, ")")
            else:
                erro(proxToken, "(")
        else:
            erro(proxToken, "while")

    elif proxToken[0] == 'ID':
        proxToken = lex(i)
        pilha.append("ID")
        if proxToken[0] == ':=':
            proxToken = lex(i)
            pilha.append(":=")
            pilha.append("Expr")
            Procedimento_Expr()
            if proxToken[0] == ';':
                proxToken = lex(i)
                pilha.append(";")
            else:
                erro(proxToken, ";")
        else:
            erro(proxToken, ":=")

    else:
        erro(proxToken, "if, while, repeat, ID")
    return 0


def Procedimento_Cond():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    pilha.append("Expr")
    Procedimento_Expr()
    if proxToken[0] == 'RELOP':
        proxToken = lex(i)
        pilha.append("RELOP")
        pilha.append("Expr")
        Procedimento_Expr()
    else:
        erro(proxToken, "RELOP")
    return 0


def Procedimento_Expr():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    pilha.append("Pre1")
    Procedimento_Pre1()
    pilha.append("Exprl")
    Procedimento_Exprl()
    return 0


def Procedimento_Pre1():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    pilha.append("Pre2")
    Procedimento_Pre2()
    pilha.append("Pre1l")
    Procedimento_Pre1l()
    return 0


def Procedimento_Pre2():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    pilha.append("Term")
    Procedimento_Term()
    pilha.append("Pre2l")
    Procedimento_Pre2l()
    return 0


def Procedimento_Exprl():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == '+':
        proxToken = lex(i)
        pilha.append("+")
        pilha.append("Pre1")
        Procedimento_Pre1()
        pilha.append("Expr1")
        Procedimento_Exprl()
    elif proxToken[0] == '-':
        proxToken = lex(i)
        pilha.append("-")
        pilha.append("Pre1")
        Procedimento_Pre1()
        pilha.append("Expr1")
        Procedimento_Exprl()
    else:
        return 0


def Procedimento_Pre1l():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == '*':
        proxToken = lex(i)
        pilha.append("*")
        pilha.append("Pre2")
        Procedimento_Pre2()
        pilha.append("Pre1l")
        Procedimento_Pre1l()
    elif proxToken[0] == '/':
        proxToken = lex(i)
        pilha.append("/")
        pilha.append("Pre2")
        Procedimento_Pre2()
        pilha.append("Pre1l")
        Procedimento_Pre1l()
    else:
        return 0


def Procedimento_Pre2l():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == '^':
        proxToken = lex(i)
        pilha.append("^")
        pilha.append("Term")
        Procedimento_Term()
        pilha.append("Pre2l")
        Procedimento_Pre2l()
    else:
        return 0


def Procedimento_Term():
    global proxToken, pilha
    printarpilha(pilha)
    pilha.pop()
    if proxToken[0] == 'num':
        proxToken = lex(i)
        pilha.append("num")
    elif proxToken[0] == 'ID':
        proxToken = lex(i)
        pilha.append("ID")
    elif proxToken[0] == '(':
        proxToken = lex(i)
        pilha.append("(")
        pilha.append("Expr")
        Procedimento_Expr
        if proxToken[0] == ')':
            proxToken = lex(i)
            pilha.append(")")
        else:
            erro(proxToken, ")")
    else:
        erro(proxToken, "ID, num, (")
    return 0


def printarpilha(pilha):
    for i in pilha:
        print(i, end=" ")
    print("")

    # Main
arq = open("Prog2.txt", "r")  # abre arquivo
Tab_Simb = open("Tab_Simb.txt", "w")  # limpar tabela de simbolos
Tab_Simb.close()
proxToken = ()
pilha = ['EP']
i = 1
proxToken = lex(i)
Procedimento_EP()  # Primeiro grafo
printarpilha(pilha)
if proxToken[1] != 'EOF':
    erro(proxToken, "EOF")
print("\nCodigo condiz com gramatica analisada!")
arq.close()
