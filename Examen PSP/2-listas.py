import threading
import random

NUMERO_ELEMENTOS = 1000
NUMERO_HILOS_INTERCAMBIO = 100
INTERCAMBIOS_POR_HILO = 1000

lista1 = [0] * NUMERO_ELEMENTOS
lista2 = [0] * NUMERO_ELEMENTOS
lista3 = [0] * NUMERO_ELEMENTOS

lock = threading.Lock()

def rellen_lista1(lista):
    num = 100001
    for i in range(NUMERO_ELEMENTOS):
        lista[i] = num
        num += 1
    print("funciona lista 1")

def rellen_lista2(lista):
    num = 200001
    for i in range(NUMERO_ELEMENTOS):
        lista[i] = num
        num += 1
    print("funciona lista 2")

def rellen_lista3(lista):
    for i in range(NUMERO_ELEMENTOS):
        lista[i] = 7
    print("funciona lista 3")

def intercambiar_elementos():
    for _ in range(INTERCAMBIOS_POR_HILO):
        
        index1 = random.randint(0, NUMERO_ELEMENTOS - 1)
        index2 = random.randint(0, NUMERO_ELEMENTOS - 1)
        
        numlista = random.randint(1, 3)
        numlista2 = random.randint(1, 3)
        
        with lock:
            if numlista == 1:
                if numlista2 == 2:
                    lista1[index1], lista2[index2] = lista2[index2], lista1[index1]
                    print("Valores= ",lista1[index1], lista2[index2])
                elif numlista2 == 3:
                    lista1[index1], lista3[index2] = lista3[index2], lista1[index1]
                    print("Valores= ",lista1[index1], lista3[index2])
                else:
                    lista1[index1], lista1[index2] = lista1[index2], lista1[index1]
                    print("Valores= ",lista1[index1], lista1[index2])
            elif numlista == 2:
                if numlista2 == 1:
                    lista1[index1], lista2[index2] = lista2[index2], lista1[index1]
                    print("Valores= ",lista1[index1], lista2[index2])
                elif numlista2 == 3:
                    lista2[index1], lista3[index2] = lista3[index2], lista2[index1]
                    print("Valores= ",lista2[index1], lista3[index2])
                else:
                    lista2[index1], lista2[index2] = lista2[index2], lista2[index1]
                    print("Valores= ",lista2[index1], lista2[index2])
            elif numlista == 3:
                if numlista2 == 1:
                    lista1[index1], lista3[index2] = lista3[index2], lista1[index1]
                    print("Valores= ",lista1[index1], lista3[index2])
                elif numlista2 == 2:
                    lista2[index1], lista3[index2] = lista3[index2], lista2[index1]
                    print("Valores= ",lista2[index1], lista3[index2])
                else:
                    lista3[index1], lista3[index2] = lista3[index2], lista3[index1]
                    print("Valores= ",lista3[index1], lista3[index2])
                    
            print(f"La lista{numlista}[{index1}] y la lista{numlista}[{index1}]")
                
def recorrerMultiplo():
    for i in range(NUMERO_ELEMENTOS):
        if lista1[i] % 10 == 0:
            print(lista1[i])
        if lista2[i] % 10 == 0:
            print(lista1[i])
        if lista3[i] % 10 == 0:
            print(lista1[i])

hilo_relleno1 = threading.Thread(target=rellen_lista1, args=(lista1,))
hilo_relleno2 = threading.Thread(target=rellen_lista2, args=(lista2,))
hilo_relleno3 = threading.Thread(target=rellen_lista3, args=(lista3,))

hilo_relleno1.start()
hilo_relleno2.start()
hilo_relleno3.start()
hilo_relleno1.join()
hilo_relleno2.join()
hilo_relleno3.join()


hilos_intercambio = []
for _ in range(NUMERO_HILOS_INTERCAMBIO):
    hilo = threading.Thread(target=intercambiar_elementos)
    hilos_intercambio.append(hilo)
    hilo.start()

hilo_multiplo = threading.Thread(target=recorrerMultiplo)

hilo_multiplo.start()
hilo_multiplo.join()
for hilo in hilos_intercambio:
    hilo.join()


suma_lista1 = sum(lista1)
suma_lista2 = sum(lista2)
suma_lista3 = sum(lista3)
suma_total = suma_lista1 + suma_lista2 + suma_lista3

print(f"Suma de lista1: {suma_lista1}")
print(f"Suma de lista2: {suma_lista2}")
print(f"Suma de lista3: {suma_lista3}")
print(f"Suma total: {suma_total}")