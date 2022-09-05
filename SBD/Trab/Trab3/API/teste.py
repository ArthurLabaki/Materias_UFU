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
                    print('ERRO')
                    return ("' ErrorMsg = " + str(error))

        if index == 2:
            print("Data de nascimento (XXXX-XX-XX): ")
            n = input()
            sqlupdate = """UPDATE aluno SET data_nasc = %(wname)s WHERE id_alu = %(wid_alu)s """
            sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
            try:
                THETABLE.execute(sqlupdate)
            except Exception as error:
                print('ERRO')
                return ("' ErrorMsg = " + str(error))

        if index == 3:
            print("CRA: ")
            n = input()
            if n > 100 or n < 0:
                print("CRA invalido!")
            else:
                sqlupdate = """UPDATE aluno SET cra = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print('ERRO')
                    return ("' ErrorMsg = " + str(error))

        if index == 4:
            print("Telefone (XXXXXXXXX): ")
            n = input()
            sqlupdate = """UPDATE aluno SET telefone = %(wname)s WHERE id_alu = %(wid_alu)s """
            sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
            try:
                THETABLE.execute(sqlupdate)
            except Exception as error:
                print('ERRO')
                return ("' ErrorMsg = " + str(error))

        if index == 5:
            print("Impossivel de alterar a faculdade, é necessario o rematriculamento!")

        if index == 6:
            print("Id do professor de Iniciação Cientifica: ")
            n = input()
            if n < 0:
                print("ID invalido!")
            else:
                sqlupdate = """UPDATE aluno SET id_prof = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print('ERRO')
                    return ("' ErrorMsg = " + str(error))

        if index == 7:
            print("Nota: ")
            n = input()
            if n > 100 or n < 0:
                print("Nota invalida!")
            else:
                sqlupdate = """UPDATE matricula SET nota = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print('ERRO')
                    return ("' ErrorMsg = " + str(error))

        if index == 8:
            print("Falta: ")
            n = input()
            if n < 0 or n > 50:
                print("Número de Faltas invalido!")
            else:
                sqlupdate = """UPDATE matricula SET falta = %(wname)s WHERE id_alu = %(wid_alu)s """
                sqlupdate = sqlupdate % {'wname': n, 'wid_alu': id}
                try:
                    THETABLE.execute(sqlupdate)
                except Exception as error:
                    print('ERRO')
                    return ("' ErrorMsg = " + str(error))