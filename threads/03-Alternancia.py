import threading

def escribeY():
    for i in range(1000):
        print("y", end="")
    
print("inicio")

t = threading.Thread(target=escribeY)

t.start()

for i in range(1000):
    print("X",end="")