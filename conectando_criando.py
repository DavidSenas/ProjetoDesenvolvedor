import sqlite3
try:
    bd = sqlite3.connect("banco_dados")
    cursor = bd.cursor()
except:
    print("Erro na criação do banco")
else:
    print("Banco criado com sucesso")
