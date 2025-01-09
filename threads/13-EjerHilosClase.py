import threading
import random

class miHilo (threading.Thread):
    def __init__(self,min_val,max_val):
        super(miHilo,self).__init__()
        self.min_val = min_val
        self.max_val = max_val
    
    def run(self):
        for i in range(self.min_val,self.max_val):
            print(i)

listaHilos = []

for i in range(10):
    min_val  = random.randint(3, 9)
    max_val  = random.randint(10, 15)
    t = miHilo(min_val,max_val)
    listaHilos.append(t)

for h in listaHilos:
    h.start()
