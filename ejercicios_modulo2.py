# 1: El Validador de Inventario (Condicionales)
cantidad_recibida = int(input("Ingrese la cantidad recibida en piezas: "))
if cantidad_recibida > 100:
    print("Inventario excedido, mover a zona B")
elif cantidad_recibida >= 50 and cantidad_recibida <= 100:
    print("Cantidad óptima")
elif cantidad_recibida < 50 and cantidad_recibida > 0:
    print("Inventario bajo, reabastecer")
else:
    print("Error: Cantidad no válida")
print("**" * 20)
# 2: Monitoreo de Stock (Ciclo while)
stock = 200
while stock >= 20:
    print(f"El stock actual es {stock}")
    stock -= 15
print("Alerta: Stock crítico. Proceder a compra")
print("**" * 20)
# 3: Clasificación de Productos (Ciclos for y Listas)
productos = ["A1", "B2", "A3", "C4", "A5"]
for i in productos:
    if i[0] == "A":
        print(f"Producto {i}: PRIORIDAD ALTA")
    else:
        print(f"Producto {i}: Stock normal")
print("**" * 20)
# 4: Cálculo de Valor de Inventario (Operaciones en Listas)
precios = [10.50, 20.0, 5.75, 50.0]
total_inventario = 0
for i in precios:
    total_inventario += i
    print(f"Al sumar ${i} el total en pesos del inventario es de ${total_inventario}")
print(f"El valor actual del inventario es ${total_inventario}")
print("**" * 20)
# 5: Buscador de Faltantes (Listas y Rompimiento de ciclos)
niveles = [40, 15, 0, 32, 10]
for nivel in niveles:
    if nivel == 0:
        print("¡Paro de línea! Producto con stock cero encontrado.")
        break
    print(f"Nivel {nivel} verificado")
print("**" * 20)
# 6: Limpieza de Datos (Instrucción continue)
datos = [100, None, 250, "Error", 300]
for dato in datos:
    if dato == None or dato == "Error":
        print("Error")
        continue
    else:
        print(f"Procesando valor:{dato}")
print("**" * 20)
# 7: Diccionarios de Almacén (Estructura Clave-Valor)
producto = {"codigo": "A101", "stock": 50, "precio": 15.5}
print(producto["stock"])
producto["stock"] = 40
print(producto)
print("**" * 20)
