import threading 

millon_de_elementos = [0] * 1000000

lock = threading.Lock()

def llenar_lista():
    for i in range(1000000):
        with lock:
            millon_de_elementos[i] = i + 1


def calcular_suma():
    suma = 0
    for i in range(999999, -1,-1):
        with lock:
            suma += millon_de_elementos[i]
        
    print("suma calculada por el segundo hilo: ",suma)

hilo_llenado = threading.Thread(target=llenar_lista)
hilo_suma = threading.Thread(target=calcular_suma)

hilo_llenado.start()
hilo_suma.start()

hilo_llenado.join()
hilo_suma.join()
