# Condicional Simple (if)
temperatura = 28
if temperatura > 30:
    print("¡Alerta! Temperatura alta. Activar enfriamiento.")
else:
    print("Temperatura controlada")
    
# Entrada de Datos y Conversión (input e int)
edad = int(input("Ingresa tu edad: "))
if edad >= 65:
    print("Este sistema no es para adultos mayores")
elif edad >= 18:
    print("Bienvenido. Tienes acceso al sistema completo.")
else:
    print("Acceso denegado. Eres menor de edad.")
    