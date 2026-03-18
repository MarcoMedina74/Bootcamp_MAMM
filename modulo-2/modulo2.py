# # 1: El Condicional if
# animal = input("indique el nombre de un animal: ")
# animal = animal.capitalize()
# if animal == "Perro":
#     print("Guau")
# elif animal == "Gato":
#     print("Miau")
# elif animal == "Vaca":
#     print("Muu")
# else:
#     print("No conozco su sonido")
# # 3: Valor absoluto (Continuación del archivo)
# entero = int(input("Indique un número: "))
# if entero < 0:
#     entero = entero * -1
# print(f"su valor absoluto es {entero}")
# 4: Números pares e impares
# numero = int(input("Ingrese un número entero: "))
# if numero % 2 == 0:
#     print("el número es par")
# else:
#     print("el número es impar")
# 5: Calculadora de Descuentos
# compra = float(input("Indique el monto de su compra en pesos: "))
# if compra > 1000:
#     descuento = compra * 0.20
#     total_a_pagar = compra - descuento
#     print(f"Su compra es de ${compra:.2f}")
#     print(f"Su descuento es de ${descuento:.2f}")
#     print(f"El total a pagar es ${total_a_pagar:.2f}")
# elif compra > 500 and compra <= 1000:
#     descuento = compra * 0.10
#     total_a_pagar = compra - descuento
#     print(f"Su compra es de ${compra:.2f}")
#     print(f"Su descuento es de ${descuento:.2f}")
#     print(f"El total a pagar es ${total_a_pagar:.2f}")
# else:
#     print(f"Su compra no aplica ningún descuento. El total a pagar es ${compra:.2f}")
# print(" ** " * 10)
# 6: Número Positivo, Negativo o Cero
# numero = int(input("Escribe un número: "))
# if numero > 0:
#     print("el número es positivo")
# elif numero < 0:
#     print("el número es negativo")
# else:
#     print("el número es cero")

# 7: Clasificación de Edades
# edad = int(input("Ingrese su edad en años: "))
# if edad < 13:
#     print("eres un niño")
# elif edad >= 13 and edad <= 17:
#     print("eres un adolescente")
# elif edad >= 18 and edad <= 115:
#     print("eres un adulto")
# else:
#     print("Edad equivocada")
# Recorrido de Listas
# frutas = ["Manzana", "Pera","Uva"]
# for i in frutas:
#     print(f"Yo como {i}")
# Filtro de caracteres
# frase = "Python es divertido"
# for letra in frase:
#     if letra == " ":
#         continue
#     else:
#         print(letra)
# Comprensión de listas
# numeros = [1, 2, 3, 4, 5]
# cuadrados = [i * i for i in numeros]

# print(f"Los números: {numeros}, al cuadrado, son: {cuadrados}")
