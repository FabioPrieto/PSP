import threading

def hiloApellido(name):
    print(name + " Rodriguez")

nombres = ["oscar","Alexandre","Lua","Carlys"]

hilos = list()
for n in nombres:
    t = threading.Thread(target=hiloApellido, args=(n,))
    hilos.append(t)
    t.start()