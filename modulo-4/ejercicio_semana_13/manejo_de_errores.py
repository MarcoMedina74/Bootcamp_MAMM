"""
    Validación de Nombre y Apellido
    """
while True:
    nombre = input("introduce tu nombre: ")
    apellido = input("introduce tu apellido: ")
    if nombre == "":
        print("no has introducido tu nombre")
    elif apellido == "":
        print("no has introducido tu apellido")
    else:
        break
while True:
    try:
        edad = int(input("introduce tu edad: "))
        break
    except ValueError:
        print("debes introducir un número")
correo = input("introduce tu correo: ")
while True:
    try:
        telefono = input("introduce tu teléfono: ")
        int(telefono)
        break
    except ValueError:
        print("debes introducir un número")

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Correo: {correo}")
print(f"Teléfono: {telefono}")

with open("datos.txt","w") as archivo:
    archivo.write(nombre+ "\n")
    archivo.write(apellido+ "\n")
    archivo.write(str(edad)+ "\n")
    archivo.write(correo+ "\n")
    archivo.write(telefono+ "\n")
    