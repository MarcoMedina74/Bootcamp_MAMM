# 1: Limpieza de Datos Maestros (Strings)
#.strip()	Elimina los espacios en blanco al inicio y al final de la cadena de texto.
# .title()	Convierte la primera letra de cada palabra a mayúscula.
# replace(" ","")	Elimina el espacio intermedio ( ) entre las palabras
pais_estandar =input("Ingrese el país:" ).strip().replace(" ","").title()
print(pais_estandar)

# 4: Conversión Forzada (Strings)
clave_producto_limpia = input("Ingrese la clave: ").strip().lower()
print(clave_producto_limpia)

# Creación de Registro (F-Strings y Archivos)
pais = input("Escriba el país: ").strip().title()
print(pais)
nombre = input("Escriba su nombre: ").strip().title()
print(nombre)
# 1: Variables y F-Strings
producto = "Tornillo M8"
cantidad = 2500
mensaje_almacen = f"La cantidad actual en stock es de {cantidad} unidades del producto {producto}."
print(mensaje_almacen)
# Guardado Básico de Datos
# sintaxis es: with open(<nombre_del_archivo>, <modo_de_apertura>) as <variable_archivo>:
## <nombre_del_archivo>: El nombre que le das al archivo de texto (ejemplo: "datos.txt").
## <modo_de_apertura>: Una letra que indica lo que quieres hacer.
   #'r' (Read / Leer): Para ver el contenido.
    # 'w' (Write / Escribir): Para crear un archivo nuevo o sobrescribir (borrar todo) uno existente. 

    # 'a' (Append / Añadir): Permite agregar nuevos datos al final del archivo sin borrar lo anterior. Este es el modo que usaremos.
## <variable_archivo>: Un nombre temporal (ejemplo: archivo) que usarás dentro del bloque para referirte al archivo y darle órdenes (como escribir).
with open("inventario.txt","a") as archivo:
    archivo.write(pais)
    archivo.write("\n")
# 3a: Registro de Códigos
ubicacion = "A12-PISO03"
with open("codigos.txt","a") as archivo:
    archivo.write(f"{ubicacion.lower()},\n")
