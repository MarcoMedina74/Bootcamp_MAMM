# 1. Longitud de una frase.
## Indicación: Identificar la longitud de una palabra ingresada.
## Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras,
## se debe imprimir un mensaje que indique que la palabra es correcta. 

# Se solicita al usuario ingresar una palabra
palabra = input("ingrese la palabra clave: ")
# Se usa la función len() para contar el número de elementos de la variable.
longitud = len(palabra)

# definir qué pasa si la palabra tiene menos de 4 letras.
if longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")

# definir qué pasa si la palabra tiene más de 8 letras.
elif longitud > 8:
    print(f"Sobran letras. Tiene {longitud} letras")
else:
    print(f"la palabra es correcta. Tiene {longitud} letras")
#############################################
# 2: Encuentra el cuadrante
## Dato importante: En las coordenadas el primer dígito es el eje "X" y el segundo es el eje "Y".

# El Plano Cartesiano: Se divide en 4 regiones llamadas cuadrantes:
## Cuadrante I: X es positivo (➕), Y es positivo (➕)
## Cuadrante II: X es negativo (➖), Y es positivo (➕)
## Cuadrante III: X es negativo (➖), Y es negativo (➖)
## Cuadrante IV: X es positivo (➕), Y es negativo (➖)

# Solicitar los datos al usuario.
eje_x = int(input("Ingrese ubicación de X expresada en número: "))
eje_y = int(input("Ingrese ubicación de Y expresada en número: "))

# Validar que ninguna coordenada sea cero.
if eje_x == 0 or eje_y == 0:
    print("las coordenadas no pueden ser cero")
# Definir el cuadrante I
elif eje_x > 0 and eje_y > 0:
    print("Tu coordenada se encuentra en el Cuadrante I")
# Definir el cuadrante II
elif eje_x < 0 and eje_y > 0:
    print("Tu coordenada se encuentra en el Cuadrante II")
# Definir el cuadrante III
elif eje_x < 0 and eje_y < 0:
    print("Tu coordenada se encuentra en el Cuadrante III")
# Definir el cuadrante IV
elif eje_x > 0 and eje_y < 0:
    print(f"Tu coordenada se encuentra en el Cuadrante IV")