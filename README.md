# Bootcamp_MAMM
Códigos del bootcamp Fundamento de Ciencia de Datos, de Marco Antonio Medina
## Proyecto: Calculadora de Índice de Masa Corporal (IMC)

### Proceso de Desarrollo y Desafíos Superados

Este programa fue desarrollado para practicar los fundamentos de Python, enfocándose en la captura segura de datos y la implementación de lógica condicional compleja.

**Desafíos y Soluciones Implementadas:**

1.  **Validación de Datos (Requisito Crítico):**
    * **Problema:** Asegurar que el usuario no dejara campos de texto vacíos y que la edad, peso y estatura fueran cifras válidas.
    * **Solución:** Se implementó un ciclo **`while`** (*bucle*) para forzar la entrada de datos hasta que fuera correcta. Para los datos numéricos (edad, peso, estatura), se utilizó el bloque **`try/except`** (Manejo de Excepciones) para atrapar (`catch`) el error si el usuario introducía texto en lugar de números.

2.  **Cálculo y Clasificación:**
    * **Cálculo del IMC:** Se utilizó el **Operador de Potencia** (`**`) para calcular la estatura al cuadrado.
    * **Clasificación Condicional:** Se implementó la lógica de clasificación de IMC (Peso Bajo, Normal, Sobrepeso, etc.) mediante una estructura anidada de **`if/elif/else`** (Condicionales Anidadas). Esta estructura asegura que solo una categoría sea seleccionada por cada valor de IMC.

3.  **Salida de Datos:**
    * Se utilizó la sintaxis de **Cadenas f** (`f-strings`) para una impresión de datos limpia, concisa y fácil de leer.

---