from threading import Lock,Thread
import time

g = 0

def sumaUno():
    global g 
    a = g
    time.sleep(0.001)
    g = a + 1

def sumaTres():
    global g 
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