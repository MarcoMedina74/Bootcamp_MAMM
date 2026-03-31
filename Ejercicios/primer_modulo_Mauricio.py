# 1: Fundamentos de Datos (Semana 1)
# Crea tres (3) variables en Python:
id_material = 20543
descripcion = "Válvula Reguladora P01"
centros_distribucion = ["CDMX", "MTY", "GDL"]

# 2: Control de Flujo (Semana 2)
# Aplicar las estructuras condicionales (If/Else/Elif)
stock_actual = 85
if stock_actual > 100:
    print("Stock Alto. Pedido Bloqueado.")
elif stock_actual > 50:
    print("Stock Medio. Revisar en 7 días.")
else:
    print("Stock Crítico. Generar Orden de Compra.")
    
# Reforzar el concepto de Bucle (Loop)
materiales_a_revisar = ["20543", "18092", "95021"]
for i in materiales_a_revisar:
    print(f"Revisando datos maestros del material: {i}")
    
# 3: Análisis de Datos con Pandas (Semana 3)
# Importar la biblioteca Pandas y crear un DataFrame
import pandas as pd
datos = {"material": [1001, 1002, 1003], "stock":[150,45,210], "unidad":["KG","PZA","LT"] }
## "Para crear el DataFrame necesitas llamar a la función DataFrame()
## de la biblioteca pd y pasarle tu variable datos."

df_inventario = pd.DataFrame(datos)

# 4: Concepto Clave de Aprendizaje Automático (Semana 4)
## Carga de Datos (Pandas) y Visualización
import pandas as pd
df_proveedores = pd.read_excel("Proveedores 12DIC25.xlsx")
df_proveedores.head()
print(df_proveedores)

# 8: Tipos de Datos (T de ETL)
print(df_proveedores.dtypes)