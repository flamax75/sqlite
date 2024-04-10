import requests
import sqlite3


def create_poquedex_database():
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    cursor.execute('drop table if exists pokemon')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS pokemon (
                   id integer Primary Key,
                   name Text,
                   type Text
                   )
    ''')

    conn.commit()
    conn.close()


def insert_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100"
    response = requests.get(url)
    data = response.json()
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    for entry in data['results']:
        pokemon_name = entry['name']
        pokemon_url = entry['url']

        pokemon_data = requests.get(pokemon_url).json()

        types = [t['type']['name'] for t in pokemon_data['types']]

        types_str = ', '.join(types)

        cursor.execute(
            "INSERT INTO pokemon (name,type) VALUES (?,?)", (pokemon_name, types_str))

    conn.commit()
    conn.close()


def visualizar_Pokemon():
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name,type FROM pokemon")
    pokemon_entries = cursor.fetchall()
    conn.close()

    for entry in pokemon_entries:
        print("Nombre: ", entry[0])
        print("Tipo: ", entry[1])
        print("------------")


def count_pokemon_by_type():
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT type ,count(*) FROM pokemon group by type")
    type_counts = cursor.fetchall()
    conn.close()


def count_pokemon_by_type():
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT type ,count(*) FROM pokemon group by type")
    type_counts = cursor.fetchall()
    conn.close()

    for entry in type_counts:
        print(f"Tipo : {entry[0]}, Cantidad :{entry[1]}")


def show_pokemon_by_type(type_name):
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name from pokemon where type = ?", (type_name,))
    type_counts = cursor.fetchall()
    conn.close()

    for entry in type_counts:
        print("Nombre : ", entry[0])


def main():
    create_poquedex_database()
    insert_pokemon_data()

    while True:
        print("Menu: ")
        print("1: Visualizar Pokemon")
        print("2: Contanilizar Pokemon por tipo")
        print("3: Mostrar Pokemon por tipo")
        print("4: Salir ")

        choise = input("Seleciona una opcion  :")
        if choise == "1":
            visualizar_Pokemon()
        elif choise == "2":
            count_pokemon_by_type()
        elif choise == "3":
            type_name = input("Dime la tipologia de pokemon")
            show_pokemon_by_type(type_name,)

        elif choise == "4":
            print("Saliendo del programa....")
            break
        else:
            print("Ninguna opcion valida")


if __name__ == "__main__":
    main()
