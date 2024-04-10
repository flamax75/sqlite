import sqlite3
con = sqlite3.connect("usuarios.db")
cursor = con.cursor()
cursor.execute('SELECT * FROM usuarios')
lineas = cursor.fetchall()
for registro in lineas:
    print(registro)

con.close()
