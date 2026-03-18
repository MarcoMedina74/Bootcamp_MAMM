"""
Escribir un Programa para graficar ventas, que pida:
El año inicial, el año final y luego las ventas de cada año para graficarlas
"""
import matplotlib.pyplot as plt

anio_inicial = int(input("Indique el año inicial con 4 dígitos: "))
anio_final = int(input("Indique el año final con 4 dígitos: "))
ventas = []
for anio in range(anio_inicial, anio_final + 1):
    venta = float(input(f"Indique las ventas del año {anio} con dos decimales: "))
    ventas.append(venta)
    
plt.plot(range(anio_inicial, anio_final + 1), ventas)
plt.title("Ventas del 2015 al 2022")
plt.xlabel("Año")
plt.ylabel("Ventas")
plt.show()
