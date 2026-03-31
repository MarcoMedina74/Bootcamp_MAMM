# 1: Variables y Operaciones
stock_inicial = 500
unidades_vendidas = 125
stock_final = stock_inicial -unidades_vendidas
print(f"Se vendieron {unidades_vendidas} piezas")
print(f"El inventario actual es: {stock_final} piezas\n")
# 2: Captura de Datos y Condicionales Simples
monto = int(input("Ingrese el monto total del pedido: "))
if monto < 100:
    print("Pedido rechazado. El mínimo es $100.\n")
else:
    print(f"Pedido de ${monto} será procesado ¡Gracias!\n")
# 3: Condicionales Compuestos y Tipos de Datos
antiguedad = int(input("Ingresa la antigüedad del producto, en años: "))
if antiguedad >= 5 and antiguedad < 10:
    print("Clasificación B: Stock Obsoleto.\n")
elif antiguedad < 5:
    print("Clasificación A: Stock Activo.\n")
else:
    print("Clasificación C: Stock a Depurar.\n")
# 4: Ciclo while (Mientras)
contrasena_maestra = "jefe123"
while True:
    intento = input("Ingrese la contraseña: ")
    if intento == contrasena_maestra:
        print("Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")

 # 5: Ciclo for (Para) y Rangos
for i in range(101,111):
     print(f"ID Almacén Generado: {i}")

# boot
animal = input("Dime un animal: ")
if animal == "perro":
    print("Guau")
else:
    print("Conozco pocos animales")
    
# ciclo
print("Impares menores a 10")
x = 1
while x <= 10:
    print(x)
    x += 2
# Random
import random
valor_simulado = random.randint(1,100)
print(valor_simulado)
# 7: Condicionales Anidados y Simulación
volumen_lote = random.randint(100,1000)
temp_lote = random.randint(10,40)
if volumen_lote > 500:
    if temp_lote > 30:
        print("Alerta CRÍTICA: Alto volumen y sobrecalentamiento.")
    else:
        print("Alerta Media: Volumen alto, temperatura normal.")
else:
    print("Volumen bajo, lote OK.")