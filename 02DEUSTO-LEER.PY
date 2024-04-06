import sqlite3

# Conectar a la base de datos
con = sqlite3.connect("grups.db")
print("Conexión establecida")
# Crear un cursor para ejecutar comandos SQL
cursor = con.cursor()

# Consulta SQL para seleccionar todos los registros de la tabla "rock"
cursor.execute("SELECT * FROM rock")

# Obtener todos los registros seleccionados
registros = cursor.fetchall()

# Imprimir los registros
print("Tabla rock:")
for registro in registros:
    print(registro)

# Cerrar la conexión con la base de datos
con.close()
