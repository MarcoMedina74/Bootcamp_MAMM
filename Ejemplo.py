# 4: Ciclo while (Mientras)
correct_pasword = "masterdata"
actual_pasword = ""
while actual_pasword != correct_pasword:
  if actual_pasword != "":
    print("Pasword incorrecto. Intenta de nuevo.")
  actual_pasword = input("Introduzca el password: ")
print("¡Acceso Autorizado! Bienvenido, Jefe de Datos.")