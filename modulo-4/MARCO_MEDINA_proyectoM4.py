# =============================================
# Proyecto M4 — Pokédex
# Autor: Marco Medina
# =============================================
#
# Construirás una Pokédex obteniendo datos de https://pokeapi.co/
#
# Reto:
# 1. Pedir al usuario el nombre de un Pokémon
# 2. Si no existe, mostrar mensaje de error
# 3. Si existe, mostrar: peso, tamaño, movimientos, habilidades y tipos
# 4. Guardar la información en un archivo .json dentro de una carpeta "pokedex"
# 5. Subir el código a GitHub con README explicando el proyecto
# =============================================

import requests
import os
import json
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image

# Le pido al usuario el nombre del Pokémon
nombre = input("Escribe el nombre de un Pokémon: ").lower().strip()
# Construyo la URL con el nombre que escribió el usuario
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
# Hago la petición a la API
respuesta = requests.get(url)

# Valido si el Pokémon existe
if respuesta.status_code != 200:
    print(f"\nEl Pokémon '{nombre}' no fue encontrado. Verifica el nombre.")
else:
     # Convierto la respuesta a un diccionario
    datos = respuesta.json()
    # Extraigo los datos que necesito
    peso = datos["weight"]
    altura = datos["height"]
    # Extraigo los tipos
    tipos = [t["type"]["name"] for t in datos["types"]]

    # Extraigo las habilidades
    habilidades = [h["ability"]["name"] for h in datos["abilities"]]

    # Extraigo los primeros 5 movimientos
    movimientos = [m["move"]["name"] for m in datos["moves"][:5]]

    # Muestro los datos básicos
    print(f"\n=== {nombre.capitalize()} ===")
    print(f"Peso: {peso} hectogramos")
    print(f"Altura: {altura} decímetros")
    print(f"Tipos: {', '.join(tipos)}")
    print(f"Habilidades: {', '.join(habilidades)}")
    print(f"Movimientos: {', '.join(movimientos)}")
    
    # Guardo la información en un archivo .json

    # Creo la carpeta "pokedex" si no existe
    os.makedirs("pokedex", exist_ok=True)

    # Preparo los datos a guardar
    info_pokemon = {
        "nombre": nombre,
        "peso": peso,
        "altura": altura,
        "tipos": tipos,
        "habilidades": habilidades,
        "movimientos": movimientos
    }

    # Guardo el archivo
    with open(f"pokedex/{nombre}.json", "w") as archivo:
        json.dump(info_pokemon, archivo, indent=4)

    print(f"\nInformación guardada en pokedex/{nombre}.json")
    # Obtengo y muestro la imagen del Pokémon
    try:
        from PIL import Image
        url_imagen = datos["sprites"]["front_default"]
        imagen = Image.open(urlopen(url_imagen))
        plt.title(nombre.capitalize())
        plt.imshow(imagen)
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"\nError: {e}")
        print(f"\n{nombre.capitalize()} no tiene imagen disponible.")