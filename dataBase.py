import mysql.connector as connector

db = connector.connect(
    host = "localhost",
    user = "gosha_krovsh",
    passwd = "",
    database = "MapaApp"
)

cursor = db.cursor()
cursor.execute('SELECT name FROM Towns')
print(cursor.next())

db.close()
