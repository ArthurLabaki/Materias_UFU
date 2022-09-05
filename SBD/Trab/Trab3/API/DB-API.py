#!/usr/bin/python
import psycopg2  # implement Python DB API 2.0
DBPARAMETERS = {'host': '*', 'database': '*', 'user': '*', 'password': '*'}

# PREPARAR A CONEXÃO


def pgconnect():
    conn = None
    try:
        conn = psycopg2.connect(**DBPARAMETERS)  # connect
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        return conn


# ABRE A CONEXÃO
DBPARAMETERS['host'] = '200.131.206.13'
DBPARAMETERS['database'] = 'arthur_labaki'
DBPARAMETERS['user'] = 'arthur_labaki'
DBPARAMETERS['password'] = 'arthurufu2021'
PGCONN = pgconnect()
THETABLE = PGCONN.cursor()
THETABLE.execute("SET search_path TO universidade")

# CONSULTA


def cons():
    print('ID: ')
    id = input()
    sqlselect = """SELECT * FROM aluno, matricula WHERE aluno.id_alu = matricula.id_alu AND aluno.id_alu = %(wid_alu)s """
    sqlselect = sqlselect % {'wid_alu': id}
    try:
        THETABLE.execute(sqlselect)
        myresult = THETABLE.fetchall()
        myrow = myresult[0]
        print(myrow)
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return ("' ErrorMsg = " + str(error))

# INSERIR


def add():
    print('ID: ')
    id = int(input())
    print('Nome: ')
    nome = input()
    print('Data de nascimento: ')
    data = input()
    print('CRA: ')
    cra = input()
    print('Telefone: ')
    tel = input()
    print('Sigla da Faculdade: ')
    facul = input()
    print('Id do Professor de IC: ')
    id_prof = input()
    print('Notas: ')
    nota = input()
    print('Faltas: ')
    falta = input()
    sqlinsert = """INSERT INTO aluno (id_alu, nome, data_nasc, cra, telefone, sigla_fac, id_prof) VALUES ('%(wid_alu)s', '%(wnome)s', '%(wdata)s', '%(wcra)s', '%(wtel)s', '%(wfacul)s', '%(wid_prof)s')"""
    sqlinsert = sqlinsert % {'wid_alu': id, 'wnome': nome, 'wdata': data,
                             'wcra': cra, 'wtel': tel, 'wfacul': facul, 'wid_prof': id_prof}
    try:
        THETABLE.execute(sqlinsert)
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return(" ErrorMsg = " + str(error))

    sqlinsert = """INSERT INTO matricula (id_alu, notas, faltas) VALUES ('%(wid_alu)s', '%(wnotas)s', '%(wfaltas)s')"""
    sqlinsert = sqlinsert % {'wid_alu': id, 'wnotas': nota, 'wfaltas': falta}
    try:
        THETABLE.execute(sqlinsert)
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return(" ErrorMsg = " + str(error))
    print("Adicionado com sucesso!")


def delete():
    print('ID')
    id = input()
    sqldelete = """DELETE FROM matricula WHERE id_alu = %(wid_alu)s """
    sqldelete = sqldelete % {'wid_alu': id}
    try:
        THETABLE.execute(sqldelete)
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return ("' ErrorMsg = " + str(error))

    sqldelete = """DELETE FROM aluno WHERE id_alu = %(wid_alu)s """
    sqldelete = sqldelete % {'wid_alu': id}
    try:
        THETABLE.execute(sqldelete)
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return ("' ErrorMsg = " + str(error))
    print("Deletado com sucesso!")


def updt():
    print('ID')
    id = input()
    loop2 = True
    while loop2:
        print("Modificar: \n1 - Nome \n2 - Data de nascimento \n3 - CRA \n4 - Telefone \n5 - Faculdade atual \n6 - Id do prof de IC \n7 - Nota \n8 - Falta \n0 - Concluir")
        index = int(input())
        if index == 1:
            print("Nome: ")
            n = input()
            if len(n) > 30 or len(n) < 0:
                print("Nome invalido!")
            else:
                sqlupdate = """UPDATE aluno SET nome = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print(" ErrorMsg = " + str(error))
                    return ("' ErrorMsg = " + str(error))

        if index == 2:
            print("Data de nascimento (XXXX-XX-XX): ")
            n = input()
            sqlupdate = """UPDATE aluno SET data_nasc = %(wname)s WHERE id_alu = %(wid_alu)s """
            sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
            try:
                THETABLE.execute(sqlupdate)
            except Exception as error:
                print(" ErrorMsg = " + str(error))
                return ("' ErrorMsg = " + str(error))

        if index == 3:
            print("CRA: ")
            n = float(input())
            if n > 100 or n < 0:
                print("CRA invalido!")
            else:
                sqlupdate = """UPDATE aluno SET cra = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print(" ErrorMsg = " + str(error))
                    return ("' ErrorMsg = " + str(error))

        if index == 4:
            print("Telefone (XXXXXXXXX): ")
            n = input()
            sqlupdate = """UPDATE aluno SET telefone = %(wname)s WHERE id_alu = %(wid_alu)s """
            sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
            try:
                THETABLE.execute(sqlupdate)
            except Exception as error:
                print(" ErrorMsg = " + str(error))
                return ("' ErrorMsg = " + str(error))

        if index == 5:
            print("Impossivel de alterar a faculdade, é necessario o rematriculamento!")

        if index == 6:
            print("Id do professor de Iniciação Cientifica: ")
            n = int(input())
            if n < 0:
                print("ID invalido!")
            else:
                sqlupdate = """UPDATE aluno SET id_prof = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print(" ErrorMsg = " + str(error))
                    return ("' ErrorMsg = " + str(error))

        if index == 7:
            print("Nota: ")
            n = float(input())
            if n > 100 or n < 0:
                print("Nota invalida!")
            else:
                sqlupdate = """UPDATE matricula SET nota = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print(" ErrorMsg = " + str(error))
                    return ("' ErrorMsg = " + str(error))

        if index == 8:
            print("Falta: ")
            n = int(input())
            if n < 0 or n > 50:
                print("Número de Faltas invalido!")
            else:
                sqlupdate = """UPDATE matricula SET falta = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print(" ErrorMsg = " + str(error))
                    return ("' ErrorMsg = " + str(error))

        if index == 0:
            print("Modificado com sucesso!")
            loop2 = False


def consall():
    i = 0
    sqlselect = "SELECT aluno.id_alu, nome, data_nasc, cra, telefone, sigla_fac, id_prof, notas, faltas FROM aluno, matricula WHERE aluno.id_alu = matricula.id_alu"
    try:
        THETABLE.execute(sqlselect)
        myresult = THETABLE.fetchall()
        print(
            "(ID, NOME,                            DATA DE NASCIMENTO,         CRA,             TELEFONE,    FACULDADE, ID PROF DE IC, NOTA, FALTA)")
        for myrow in myresult:
            print(myrow)
            i = i + 1
    except Exception as error:
        print(" ErrorMsg = " + str(error))
        return ("' ErrorMsg = " + str(error))
    print("Número de alunos matriculados: ", i)


loop = True
while loop:
    print("\nDigite: \n1 matricular novo aluno; \n2 deletar matricula pelo id; \n3 modificar matricula pelo id; \n4 consultar alunos pelo id; \n5 consultar todos os alunos; \n6 salvar e continuar; \n7 abortar e continuar; \n0 salvar e sair.")
    valor = int(input())
    if valor == 1:
        add()       # INSERE
    if valor == 2:
        delete()    # DELETA
    if valor == 3:
        updt()      # ATUALIZA
    if valor == 4:
        cons()      # CONSULTA 1 LINHA
    if valor == 5:
        consall()   # CONSULTA TODA A TABELA
    if valor == 0:
        loop = False  # FECHA A CONEXÃO
    if valor == 6:
        PGCONN.commit()  # SALVA DADOS
        print("Salvamento da transação efetuado no BD!")
    if valor == 7:
        PGCONN.rollback()  # RECUPERA DADOS
        print("Rollback da transação efetuado no BD!")
    if valor > 7 or valor < 0:
        print('Numero digitado invalido!')


# FECHA A CONEXÃO
print("Salvando e fechando conexção!")
PGCONN.commit()
PGCONN.close()
