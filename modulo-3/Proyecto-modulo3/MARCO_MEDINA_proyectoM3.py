"""
Programa para simular una Máquina de Galton.
Calcula el destino de 3000 canicas a través de 12 niveles de obstáculos
y muestra los resultados en un histograma.
"""
import random # Con esto se importa el módulo para generar números aleatorios
import matplotlib.pyplot as plt # Submódulo pyplot, para crear gráficas, y le pone el alias plt

CANTIDAD_CANICAS = 3000
NIVELES = 12
resultados = []

def simular_canica():
    """Función para la simulación física de una máquina de Galton, mediante la obtención de
números aleatorios 

    Returns:
        retorna los pasos a la derecha que va acumulando
    """
    pasos_derecha = 0
    
    for i in range(NIVELES):
        resultado = random.randint(0,1) # Genera un número entero aleatorio. En este caso 0 ó 1.
        if resultado == 1:
            pasos_derecha += 1
    return pasos_derecha


for vez in range(CANTIDAD_CANICAS):
    derecha = simular_canica()
    resultados.append(derecha)


def graficar_resultados(datos):
    """Función para graficar los datos
    generador por el código anterior
    que simula una Máquina de Galton
    """
    plt.hist(datos, bins = NIVELES + 1, edgecolor="black")
    """el histograma deberá generarse en base datos y bins
    """
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.show()
    """Aquí se mostrará la Campana de Gauss
    """


graficar_resultados(resultados)
