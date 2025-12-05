# 1: Validación de Stock Mínimo
stock_actual=75
stock_seguridad=50
if stock_actual < stock_seguridad:
    print("🚨 ALERTA CRÍTICA: Stock bajo el nivel de seguridad.")
elif stock_actual == stock_seguridad:
    print("⚠️ Advertencia: Stock justo en el límite de seguridad.")
else:
    print("✅ Stock OK.")

# Ejercicio 2: Función de Clasificación de Material
def clasificar_material(volumen_anual):
    if volumen_anual >= 500:
        return "A (Alto Movimiento)"
    elif volumen_anual > 100:
        return "B (Medio Movimiento)"
    else:
        return "C (Bajo Movimiento)"
volumen_anual = 650
print(f"El volumen anual indica que es un producto de la categoría: {clasificar_material(volumen_anual)}")