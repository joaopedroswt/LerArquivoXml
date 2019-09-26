import psycopg2
class Conexao:

    def conecta(self, sql):
        try:
            conn = psycopg2.connect("dbname='Sistema' "
                                    "user='postgres' "
                                    "host='127.0.0.1' "
                                    "password='4f9bba0717'")
            cur = conn.cursor()
            try:
                teste = cur.execute(sql)
               # cur.execute(sql)
               # rows = cur.fetchall()

            except:
                print("I can't drop our test database!")
        except:
            print("I am unable to connect to the database")

        return teste