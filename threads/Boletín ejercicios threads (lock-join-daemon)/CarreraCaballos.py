from threading import Thread, Lock
import random
import time

caballos = []
meta = 100
lock = Lock()
terminar = False

def avanzar(caballo_id):
    global caballos, terminar
    while not terminar:
        with lock:
            avance = random.randint(1, 5)
            caballos[caballo_id] += avance
            if caballos[caballo_id] >= meta:
                print(f"Caballo {caballo_id} gana la carrera!")
                terminar = True

num_caballos = int(input("Número de caballos: "))
caballos = [0] * num_caballos
hilos = [Thread(target=avanzar, args=(i,)) for i in range(num_caballos)]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()
