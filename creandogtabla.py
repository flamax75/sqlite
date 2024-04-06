import sqlite3


def insertar_usuarios():
    legatura = sqlite3.connect("usuarios.db")
    print("conexion establecida")
    cursor = legatura.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios(nume text , numar int)")

    valori = [("vlad", 34), ("rares", 47), ("flaviu", 48)]

    for valor in valori:
        cursor.execute("SELECT*FROM usuarios WHERE nume=? AND numar=?", valor)
        existe = cursor.fetchone()

        if not existe:
            cursor.execute("INSERT INTO usuarios VALUES (?,?)", valor)
            print(f"Registro insertado :{valor}")

        else:
            print(f"El registro{valor} ya existe ,no se insertara")

    legatura.commit()
    legatura.close()


insertar_usuarios()
