import threading

# Metodo de asicion de hilo
def Saludo():
    print("HOLA")
    print("HOLA")
    print("HOLA")
    print("HOLA")
    print("HOLA")
    print("HOLA")
    
t = threading.Thread(target=Saludo)
t.start()

print("hola") #Impresion hilo principal