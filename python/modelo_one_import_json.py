import json
import psycopg2

connection = psycopg2.connect("conexão com o banco de dados")
connection.autocommit = True
cursor = connection.cursor()

with open("arquivo.json", encoding="utf-8") as arq:
    lista_de_tuplas = [(linha,) for linha in arq]
cursor.executemany("INSERT INTO tabela (coluna) VALUES (%s)", lista_de_tuplas)