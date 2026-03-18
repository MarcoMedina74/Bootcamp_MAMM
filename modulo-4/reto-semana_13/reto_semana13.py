"""Programa para registrar alumnos, validar sus datos,
guardar sus calificaciones, calcular promedios y
mostrar la información sin que se detenga por errores de entrada."""
alumnos = {}
while True:
    print("\n***Menú***\n")
    print("(1) Agregar un nuevo alumno")
    print("(2) Ver los alumnos y las calificaciones")
    print("(S): Salir")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        while True:
            nombre = input("Escriba el nombre del alumno: ")
            if nombre != "":
                break
            print("Error: El nombre no puede estar en blanco.")
        while True:
            try:
                cantidad = int(input("¿Cuántas calificaciones desea agregar?: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        notas = []
        for i in range(cantidad):
            while True:
                try:
                    calificacion = float(input("Escriba la calificación: "))
                    notas.append(calificacion)
                    break
                except ValueError:
                    print("Error: Ingrese un valor numérico.")
            
        alumnos[nombre] = notas
        print("\nSe registró correctamente\n")
    elif opcion == "2":
        print("\n--- Estos son los promedios registrados por alumno ---\n")
        for nombre, notas_alumno in alumnos.items():
            if len(notas_alumno) > 0:
                promedio = sum(notas_alumno) / len(notas_alumno)
                promedio_redondeado = round(promedio, 2)
                print(f"{nombre}: Promedio {promedio_redondeado}")
        print("\n-" * 30)
    elif opcion == "s" or opcion == "S":
        confirmar = input("¿Está seguro de que desea salir? (S/N): ")
        if confirmar == "s" or confirmar == "S":
            print("Fin del programa.")
            break
    