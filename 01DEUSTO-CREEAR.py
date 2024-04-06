import sqlite3


def insertar_grupos():
    con = sqlite3.connect("grups.db")
    print("Conexión establecida")

    cursor = con.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS rock (nombre text ,miembros int)")

    # Lista de valores a insertar
    valores = [("KISS", 4), ("BON JOVI", 5), ("ACDC", 4),
               ("MUSE", 3), ("METALLICA", 4), ("SEPULTURA", 5)]

    for valor in valores:
        # Consultar si el registro ya existe en la base de datos
        cursor.execute(
            "SELECT * FROM rock WHERE nombre=? AND miembros=?", valor)
        existe = cursor.fetchone()

        if not existe:
            # Si el registro no existe, lo insertamos
            cursor.execute("INSERT INTO rock VALUES (?, ?)", valor)
            print(f"Registro insertado: {valor}")
        else:
            print(f"El registro {valor} ya existe, no se insertará.")

    con.commit()
    con.close()


insertar_grupos()
