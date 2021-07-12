import sqlite3
try:
    bd = sqlite3.connect("banco_dados")
    cursor = bd.cursor()
    cursor.execute("CREATE TABLE locais(cep integer, end text, bairro text, estado text)")
    bd.commit()
    cursor.execute('SELECT * FROM LOCAIS')
    for c in cursor.fetchall():
        print("===" * 20)
        for x in c:
            print(x)
except:
    print("Erro na criação do bando")
else:
    print("Banco criaçao do sucesso")

