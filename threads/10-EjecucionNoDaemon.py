from threading import *
import time

def hilo():
    for i in range(10):
        print("hilo no daemon (Foreground)")
        time.sleep(1)

t = Thread (target=hilo)
t.start()

time.sleep(5)
print("Hilo principal")