# Programa con colores del arcoíris (rojo, naranja,
# amarillo, verde, azul y violeta) y en dos idiomas diferentes.
ingles = {
    "rojo": "Red",
    "naranja": "Orange",
    "amarillo": "Yellow",
    "verde": "Green",
    "azul": "Blue",
    "violeta": "Violet"
}

frances = {
    "rojo": "Rouge",
    "naranja": "Orange",
    "amarillo": "Jaune",
    "verde": "Vert",
    "azul": "Bleu",
    "violeta": "Violet"
}
#  indicar al usuario cuáles son los dos idiomas a los que puede traducir tu programa
print("Idiomas disponibles: 1 (Inglés) o 2 (Francés)")
opcion = input("Seleccione el idioma a traducir: ")
# Procesar la frase y buscar el color en el idioma que eligió el usuario.
frase = input("Escriba una oración en español que incluya uno de los colores del arcoíris: ")
frase = frase.lower()
palabras = frase.split()
# Unir la elección del idioma con la traducción de la palabra
if opcion == "1":
    for palabra in palabras:
        if palabra in ingles:
            print(f"El color {palabra} en Inglés es: {ingles[palabra]}")
elif opcion == "2":
    for palabra in palabras:
        if palabra in frances:
            print(f"El color {palabra} en Francés es: {frances[palabra]}")
else:
    print("Opción, no válida")
