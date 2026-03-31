# Semana 5
# =======================================================
# RETO 1: VALIDADOR DE EDAD
# =======================================================
entrada = input("Ingrese su edad para verificar la venta del cigarro: ")
edad = 0 

### Validación de entrada (isnumeric)
if entrada.isnumeric():
    edad = int(entrada)
else:
    print("¡Dato incorrecto! Debes introducir un número entero, positivo")
    exit()
if edad <= 0:
    print("WOOOOOWWW!! Que joven eres. Pero, lo siento, eso no es posible")
    exit()
elif edad > 115:
    print("¡¡¡VAYA!!!! ¿Cómo le haces para vivir tanto? ¡No te creo! mejor intenta de nuevo.")
    exit()
elif edad < 18:
    print("Eres menor de edad así que no puedes comprar tu cigarro")
else:
    # Si la edad está entre 18 y 115
    print("Eres mayor de edad. Aquí tienes tu cigarro")
print(f"\n--- FIN RETO 1 ---\n")
"""
El código cumple con todos los requisitos del reto:

1. Validación de Tipo: Usa .isnumeric() y int() para asegurar que se trabaja con números.
2. Manejo de Error de Entrada: Usa exit() para detenerse si la entrada es incorrecta.
3. Lógica de Negocio Encadenada: Usa if, elif, y else en el orden correcto para validar:
   - Edad <= 0 (Imposible)
   - Edad > 115 (Exagerada)
   - Edad < 18 (Menor de edad)
   - Cualquier otro caso (Edad entre 18 y 115)
"""
# =======================================================


# =======================================================
# RETO 2: CALCULADORA DE DIFERENCIA DE AÑOS
# =======================================================

# Crear un programa que solicite dos años y calcule la diferencia, manejando casos especiales
print("\n--- INICIO RETO 2: CALCULADORA DE AÑOS ---")
#Pedir los años:
anio_actual = input("Indique el año actual: ") # Se usa 'anio' por convención (no usar "ñ")
anio_introducido = input("Indique el año a calcular: ")
# Validación y Conversión a Número
if anio_actual.isnumeric() and anio_introducido.isnumeric():
    num_actual = int(anio_actual)
    num_introducido = int(anio_introducido)
else:
    exit()
    
diferencia = num_actual -num_introducido
# Notificar si es el mismo año
if diferencia == 0:
    print("Has introducido el mismo año que el actual")
    exit()
elif diferencia > 0:
    if diferencia == 1:
        print(f"Desde el año {num_introducido} ha pasado 1 año")
    else:
        print(f"Han pasado {diferencia} años desde el año que has introducido")
else:
    # Usamos abs() para obtener la cantidad sin el signo negativo.
    diferencia_futura = abs(diferencia)
    if diferencia_futura == 1:
        print(f"Para llegar a {num_introducido} hace falta 1 año")
    else:
        print(f"Faltan {diferencia_futura} años para llegar al año que has introducido")
print("--- FIN RETO 2 ---")
# =======================================================