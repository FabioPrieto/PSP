from threading import Thread, Lock
import time

contadorAscendente = 0
contadorDescendente = 1_000_000
terminar = False
lock = Lock()

def incrementar():
    global contadorAscendente, terminar
    while not terminar:
        with lock:
            contadorAscendente += 1

def decrementar():
    global contadorDescendente, terminar
    while not terminar:
        with lock:
            contadorDescendente -= 1

def vigia():
    global contadorAscendente, contadorDescendente, terminar
    while not terminar:
        with lock:
            if contadorAscendente > contadorDescendente:
                print("Ascendente supera al Descendente")
                terminar = True

hilo1 = Thread(target=incrementar)
hilo2 = Thread(target=decrementar)
hilo3 = Thread(target=vigia)

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
