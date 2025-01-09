import threading
import time

def tarea():
    time.sleep(1)
    return

for _ in range(10): # _ significa que no accedo a ningún elemento a iterar
    threading.Thread(target=tarea).start()
    
print ("Hilos activos: ", threading.active_count())
for t in threading.enumerate():
    print (t.name)