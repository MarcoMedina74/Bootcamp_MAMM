import matplotlib.pyplot as plt
anio_inicial = int(input("Indique el año inicial con 4 dígitos: "))
anio_final = int(input("Indique el año final con 4 dígitos: "))

anios = []
ventas = []

for anio in range(anio_inicial, anio_final +1):
    print(f"El año en revisón es: {anio} ")
    anios.append(anio)
    monto = float(input(f"Indique el monto de ventas del año {anio} $"))
    ventas.append(monto)
    
plt.plot(anios, ventas)
plt.title(f"Ventas del {anio_inicial} al {anio_final}")
plt.show()