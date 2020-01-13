import json
from psycopg2.extras import Json, DictCursor
import psycopg2

connection = psycopg2.connect("dbname=nomeDoBanco user=usuario host=enderecoDoBanco password=senha port=numero")
connection.autocommit = True
cursor = connection.cursor(cursor_factory=DictCursor)

data = []
with open('C:\Code\processoSeletivo\dataSprints\data\dataTest2009.json') as f:
    for line in f:
        data.append(json.loads(line))

    for item in data:
        cursor.execute("INSERT INTO trips (info) VALUES (%s)",[Json(item)])
