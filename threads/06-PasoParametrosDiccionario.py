import threading

def hiloApellido(name, inicio=1, fin=1):
    for x in range(inicio,fin):
        print(f"{name} Rodriguez {str(x)} años\n",end="")
    

nombres = ["oscar","Alexandre","Lua","Carlys"]
hilos = list()
for n in nombres:
    t = threading.Thread(target=hiloApellido, args=(n,), kwargs={'inicio':2, 'fin':4})
    hilos.append(t)
    t.start()