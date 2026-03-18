# cuadrados método tradicional sin compresión:
# cuadrados = []
# for numero in range(10):
#     numero = numero **2
#     cuadrados.append(numero)
# print(cuadrados)
# Cuadrados con Comprensión de Listas
# cuadrados = [numero ** 2 for numero in range(10)]
# print(cuadrados)
#########################################
# Crear un diccionario por medio de la compresión de listas
# cubos = {cubo : cubo ** 3 for cubo in range(10)}
# print(cubos)
##########################################
# pares = [numero for numero in range(1,11) if numero %2 == 0]
# print(pares)
# impares =[numero for numero in range(1,11) if numero %2 != 0]
# print(impares)

nombres = ["ana", "fernando", "carlos", "priscila"]
print(nombres)
nombres = [nombre.capitalize() for nombre in nombres]
print(nombres)