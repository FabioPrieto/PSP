from threading import Lock,Thread
import time

g = 0
lock = Lock()
def sumaUno():
    global g 
    lock.acquire()
    a = g
    time.sleep(0.001)
    g = a + 1
    lock.release()

def sumaTres():
    global g 
    with lock:
        a = g
        time.sleep(0.001)
        g = a + 3
    

listaHilos = []
for func in [sumaUno,sumaTres]:
    listaHilos.append(Thread(target=func))
    listaHilos[-1].start()

for h in listaHilos:
    h.join()

print(g)