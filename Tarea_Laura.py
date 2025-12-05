# PROYECTO MODULO 1 PYTHON
## Elaboración de cálculo de índice de masa corporal (IMC)
nombre = input("Ingrese su nombre (Nombre(s), apellido paterno; apellido materno): ")
edad = input("Ingrese su edad en años?: ")
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (estatura ** 2)
print(imc)

print(f"Hola {nombre}, tiene {edad} años.")
print(f"Mide {estatura}m, pesa {peso}kg.")
print(f"Su IMC es: {imc:.2f}")
if imc < 18.5:
    print("→ Bajo peso")
elif 18.5 <= imc < 25:
    print("→ Peso normal ✓")
elif 25 <= imc < 30:
    print("→ Sobrepeso")
elif 30 <= imc < 35:
    print("→ Obesidad grado I")
elif 35 <= imc < 40:
    print("→ Obesidad grado II")
else:
    print("→ Obesidad grado III (mórbida)") [web:94]

print("Tabla de referencia de índice")
print("menor de 18.5 - bajo peso")
print("de 18.5 a 25 - peso ideal")
print("de 25 a 30 - sobre peso")
print("de 30 a 35 - obesidad grado I")
print("de 35 a 40 - obesidad grado II")
print("superior a 40 - obesidad grado III")
input("Presiona ENTER para salir...")
print("Pueba")

