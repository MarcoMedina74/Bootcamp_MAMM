#Registro y Limpieza de Lotes
lote = input("Digite el número de lote: ").strip()
with open("lotes_limpios.csv","a") as archivo:
    archivo.write(f"{lote}\n")
# 3c: Modo Sobrescribir ('w')
registro_error = "Lote 404"
with open("lotes_limpios.csv","w") as lotes:
    lotes.write(registro_error + "\n")
# 3d: Modo Lectura ('r')
with open("lotes_limpios.csv","r") as leer:
    contenido_archivo = leer.read()
print(contenido_archivo)
# Flujo Completo (Captura, Manipulación y Guardado)
codigo_mat = input("Ingresa el código de material: ").upper()
descripcion = input("Ingresa la descripción del material: ").capitalize()
with open("maestro_materiales.csv","a") as registro:
    registro.write(f"{codigo_mat}, {descripcion}\n")
# 5: Refuerzo de Vocabulario y Git
