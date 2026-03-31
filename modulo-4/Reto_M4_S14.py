# RETO DE LA SEMANA 14
#  Programa que funciona como agenda
# Debe cumplir con lo siguiente:

# El programa mostrará en la pantalla la información de los contactos enumerados
# Preguntará de cuál de los contactos se desea modificar la información.
# Se podrá modificar el nombre, el teléfono y el correo.
# Se debe actualizar la información en el archivo.
# El programa no debe interrumpirse al ingresar mal los datos o las opciones.

import os

# Define la ruta de la carpeta.
carpeta_actual = os.path.dirname(__file__)
# Une la ruta de la carpeta con el archivo.
ruta_agenda = os.path.join(carpeta_actual, "agenda.txt")

personas = []

    # Verifica si el archivo ya existe.
if os.path.exists(ruta_agenda):
        # Si existe lo abre en modo lectura:
        with open(ruta_agenda, "r") as f_agenda:
            for linea in f_agenda:
                datos = linea.strip().split()
                nuevo_contacto = [datos[0], datos[1], datos[3], datos [5], datos [7]]
                personas.append(nuevo_contacto)
                
        
while True:
    print("""
    1. Agregar persona a la agenda.
    2. Guardar datos en un archivo.
    3. Modificar contacto.
    """)
    opcion = input("Ingrese una opción: ")

    if opcion == "1":

        contacto = []
        while True:
            nombre = input("Introduce Nombre: ")
            apellido = input("Introduce Apellido: ")
            if nombre == "":
                print("No has introducido un nombre")
            elif apellido == "":
                print("No has introducido un apellido")
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break

        while True:
            try:
                edad = int(input("Introduce la edad: "))
                contacto.append(edad)
                break
            except ValueError:
                print("Debes introducir un número")

        correo = input("Introduce correo electrónico: ")
        contacto.append(correo)

        while True:
            try:
                telefono = input("Introduce el Teléfono: ")
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print("Debes introducir un número")

        personas.append(contacto)

    elif opcion == "2":
        with open('agenda.txt', 'w') as f_agenda:
            for persona in personas:
                f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Teléfono: {persona[4]}\n')
        print("Datos guardados en agenda.txt")
        break
    
    elif opcion == "3":
        if not personas:
            print("La agenda está vacía.")
        else:
            for indice , dato in enumerate(personas, 1):
                print(f"{indice}.-{dato[0]} {dato[1]} Edad: {dato[2]} Correo: {dato[3]} Teléfono: {dato[4]}\n")
            
            while True:
                try:
                    modificar = int(input("Indique el número de contacto a modificar: "))
                    indice_real = modificar -1
                    break
                except ValueError:
                    print("Debes introducir un número")
            
            nvo_nombre = input("Introduce el nombre: ")
            nvo_correo = input("Introduce correo electrónico: ")
            
            while True:
                try:
                    nvo_telefono = input("Introduce el Teléfono: ")
                    int(nvo_telefono)
                    break
                except ValueError:
                    print("Debes introducir un número")
            personas[indice_real][0] = nvo_nombre
            personas[indice_real][3] = nvo_correo
            personas[indice_real][4] = nvo_telefono
            with open('agenda.txt', 'w') as f_agenda:
                for persona in personas:
                    f_agenda.write(f"{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Teléfono: {persona[4]}\n")
    else:
        print("\n**********Opción inválida**********\n")
        print("Volver a intentar")
