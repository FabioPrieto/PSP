from threading import Thread, Lock

archivo = "archivo.txt"  # Reemplaza con tu archivo de texto
numVocalesTotal = 0
lock = Lock()

def contar_vocales(texto):
    global numVocalesTotal
    vocales = "aeiouAEIOU"
    numVocales = sum(1 for c in texto if c in vocales)
    with lock:
        numVocalesTotal += numVocales

with open(archivo, "r") as f:
    contenido = f.read()

tamaño_parte = len(contenido) // 4  # Dividir en 4 hilos
hilos = []

for i in range(4):
    parte = contenido[i * tamaño_parte: (i + 1) * tamaño_parte]
    hilo = Thread(target=contar_vocales, args=(parte,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Total de vocales:", numVocalesTotal)
