# El reto de esta semana consiste en obtener el clima de mi localidad.

# Importamos requests, que es una librería externa de Python para enviar 
# peticiones HTTP (GET, POST, etc.) de forma sencilla.

import requests

# Se guardan los datos latitud.y longitud
lat = 20.664946201910396
long = -103.27708641903585
# Se guarda el API Key
key_API = "0e95c588771a98d710366b458e73490f"

# Con las variables y sus partes se crea el URL destino de la petición GET
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={key_API}"

# Aquí se realiza la Petición GET
variable_respuesta  = requests.get(url)

# Validamos si el código de estado es 200 (Éxito/OK)
if variable_respuesta.status_code == 200:
    
    # Usamos el método .json() para convertir los datos
    # que vienen de internet 
    # a un formato que Python pueda leer como un Diccionario
    datos_clima = variable_respuesta.json()

    # Para extraer la temperatura de ese diccionario 
    # datos_clima, usamos los corchetes [] con 
    # Encadenamiento: Usamos ["main"]["temp"] para ir directo al número
    temperatura_kelvin = datos_clima["main"]["temp"]
    # Convertimos los grados Kelvin a Celsius
    temperatura_celsius = temperatura_kelvin - 273.15
    print(f"La temperatura actual en el oriente de la ciudad de Guadalajara es de {temperatura_celsius:.2f} °C\n")
else:
    print(f"Error en la petición. Código: {variable_respuesta.status_code}")