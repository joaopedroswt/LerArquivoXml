from .conexao import *
class ControllerSis:

    def controller_sis(request):
        teste = Conexao()

        insert = teste.conecta(""" insert into sis_usuarios(login,senha) VALUES('test222222','159753') """)
        select = teste.conecta(""" select * from sis_usuarios""")

        print("insert")
        print(insert)
        print(select)
        return ''
