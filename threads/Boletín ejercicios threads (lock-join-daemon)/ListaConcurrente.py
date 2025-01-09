import threading
import random

lista = []
lock = threading.Lock()
terminar = False

def añadir_numeros():
    global lista, terminar
    while not terminar:
        with lock:
            lista.append(random.randint(1, 100))

def eliminar_primero():
    global lista, terminar
    while not terminar:
        with lock:
            if lista:
                lista.pop(0)

def eliminar_ultimo():
    global lista, terminar
    while not terminar:
        with lock:
            if lista:
                lista.pop()

def mostrar_suma():
    global lista, terminar
    while not terminar:
        with lock:
            if len(lista) % 10 == 0 and lista:
                print("Suma de elementos:", sum(lista))

hilos = [
    threading.Thread(target=añadir_numeros),
    threading.Thread(target=eliminar_primero),
    threading.Thread(target=eliminar_ultimo),
    threading.Thread(target=mostrar_suma)
]

for hilo in hilos:
    hilo.daemon = True
    hilo.start()

while len(lista) < 100_000:
    pass

terminar = True
print("Fin del programa")
