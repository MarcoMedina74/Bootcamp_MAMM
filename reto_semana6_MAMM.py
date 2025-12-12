# RETO DE LA SEMANA 6 #
## Marco Medina
### Parte 1: Captura y Validación de la Primera Contraseña
contrasena_original = "" 
while True: # Cilco infinito (Mientras esto sea Verdadero, que lo serpa siempre)
    contrasena_original = input("Ingrese su contraseña: ")
    if contrasena_original[0].isdigit(): # Para verificar solo el primer carácter (el índice [0]),
        break
    else:
        print("La contraseña debe comenzar con un número")
    # Usa el primer ciclo Mientras (while True) y el método .isdigit() para asegurar que la contraseña empiece con un número.
    
### Parte 2 del reto: "Que pida ingresar nuevamente la contraseña y verificar que coincida con la primera ingresada"
### "Si se cometen tres errores al ingresar la contraseña, que despliegue un mensaje de aviso y cierre el programa".
intentos_fallidos = 0
while True:
    contrasena_confirmacion = input("Confirme su contraseña: ")
    if contrasena_original == contrasena_confirmacion:
        print("Contraseña correcta")
        break
    else:
        print("Las contraseñas no coinciden")
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Fin del programa")
            break
    
    