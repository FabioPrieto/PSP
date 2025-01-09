import threading

def actividad():
    print("Escribo desde un hilo")

print("Inicio")

hilos = list()
for i in range(50):
    t = threading.Thread(target=actividad)
    hilos.append(t)
    t.start()

print("FIN")