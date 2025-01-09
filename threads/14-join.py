import threading
import logging

logging.basicConfig(level = logging.DEBUG,
                    format='[%(threadName)-10s]:%(message)s')

def imprime_x(x,n):
    for i in range(n):
        logging.debug(x)
        
t1 = threading.Thread(target=imprime_x,args=("norte",5))
t2 = threading.Thread(target=imprime_x,args=("sur",10))

t1.start()
t2.start()

#Espera hasta que el hilo t1 haya acabado
t1.join()
#Espera hasta que el hilo t2 haya acabado
t2.join()

logging.debug("Fin!")