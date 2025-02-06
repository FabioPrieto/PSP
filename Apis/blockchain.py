import urllib.request
import json

def obtener_precio_bitcoin():
    url = "https://blockchain.info/ticker"
    with urllib.request.urlopen(url) as respuesta:
        datos = json.loads(respuesta.read().decode())
        return datos["EUR"]["last"]

precio = obtener_precio_bitcoin()
print(f"El precio actual de Bitcoin en euros es: €{precio}")
