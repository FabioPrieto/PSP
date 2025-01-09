import threading

def funcion_hilo():
    if (threading.current_thread().name == "miHilo7"):
        threading.current_thread().name = "nombre-cambiado"
    print (f"Hola desde: {threading.current_thread().name} \
    ID {threading.current_thread().ident}\n", end="")
    #threading.current_thread().ident = 666 #comprobación de error

hilos = list()
for n in range (1,11):
    t = threading.Thread(target=funcion_hilo, name="miHilo")
    if (n>5):
        t.name = "miHilo"+str(n)
    hilos.append(t)
    
for h in hilos:
    h.start()
#podemos establer una propiedad al instanciar un hilo linea 12
#podemos establecer una propiedad como métod con un hilo instanciaco 14
#podemos tener una lista de hilos y lanzarla posteriormente línea 18
#podemos saber el hilo que está ejecutando un código (función) current_thread()
#podemos leer y cambiar el nombre
#no podemos cambiar el ident (PID) que es generado por el sistema