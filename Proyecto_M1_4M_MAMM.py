# Calculadora de Índice de masa corporal 
## Reglas: Ningún dato puede quedar vacío. Edad, peso y estatura deben ser cifras.
nombre = "" # Variable vacía para que el While arranque
while nombre == "": # Corre un loop mientras nombre esté vacía
    nombre = input("Escriba su (s) Nombre (s):") #input siempre pide una cadena de texto
    if nombre == "": # Condicional si nombre está vacío
        print("ERROR: El nombre no puede estar vacío.") # Lo que imprime si se cumple la condición

apellido_paterno = ""
while apellido_paterno == "":
    apellido_paterno = input("Escriba su apellido paterno: ")
    if apellido_paterno == "":
        print("ERROR: El apellido paterno no puede estar vacío.")
        
apellido_materno = ""
while apellido_materno == "":
    apellido_materno = input("Escriba su apellido materno: ")
    if apellido_materno == "":
        print("ERROR: El apellido materno no puede estar vacío.")

# Edad
es_valido = False # Se crea esta variante para correr el while
while es_valido == False:
    try:
        edad = int(input("Indique su edad: "))
        es_valido = True 
        
    except ValueError:
        print("ERROR: La edad debe ser un número entero (cifra).")

# Peso
es_valido = False
while es_valido == False:
    try:
        peso = float(input("Indique su peso: "))
        es_valido  = True
    except ValueError:
        print("ERROR: El peso debe ser un número con decimales (cifra).")

# Estatura:
es_valido = False
while es_valido == False:
    try:
        estatura = float(input("Indique su estatura: "))
        es_valido = True
    except ValueError:
        print("ERROR: La estatura debe ser un número con decimales (cifra).")
imc = peso / (estatura ** 2)
# Luego de calcular el IMC agregué el estado del paciente, según lo indicado en la referencia del ISSSTE
## Sé que no lo pide el proyecto pero me pareció correcto incluirlo
print(f"paciente: {nombre} {apellido_paterno} {apellido_materno}.\nEdad: {edad} años.\nPeso: {peso} Kgs.\nEstura: {estatura} metros.\nIMC: {imc:.2f}")
if imc < 18.4:
    print("La condición del paciente es: Peso bajo")
elif imc < 25:
    print("La condición del paciente es: Peso normal")
elif imc < 30:
    print("La condición del paciente es: Sobrepeso")
elif imc < 35:
    print("La condición del paciente es: Obesidad Leve")
elif imc < 39:
    print("La condición del paciente es: Obesidad media")
else:
    print("La condición del paciente es: Obesidad mórbida")