import sqlite3
con = sqlite3.connect("grups.db")
cursor = con.cursor()
cursor.execute('SELECT nombre FROM rock WHERE miembros=4')
linea = cursor.fetchall()
for registro in linea:
    print(registro)

con.close()
