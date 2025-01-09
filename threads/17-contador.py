from threading import Lock,Thread
import time

g = 0
lock = Lock()

def sumaUno():
    global g 
    lock.acquire()
    for _ in range(100):
        time.sleep(0.001)
        g += 1
    lock.release()
    

listaHilos = []
for i in range(10):
    listaHilos.append(Thread(target=sumaUno))
    listaHilos[-1].start()

for h in listaHilos:
    h.join()

print(g)