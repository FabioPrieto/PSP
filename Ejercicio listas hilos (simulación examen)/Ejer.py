import threading
import random

NUMERO_ELEMENTOS = 500
NUMERO_HILOS_INTERCAMBIO = 1000
INTERCAMBIOS_POR_HILO = 100

lista1 = [0] * NUMERO_ELEMENTOS
lista2 = [0] * NUMERO_ELEMENTOS

lock = threading.Lock()  # Lock para evitar problemas de concurrencia

# Función para rellenar una lista con pares o impares
def insertar_numeros(lista, parimpar):
    num = 2 if parimpar == "par" else 1
    for i in range(NUMERO_ELEMENTOS):
        lista[i] = num
        num += 2

# Función para intercambiar valores entre listas
def intercambiar_elementos():
    for _ in range(INTERCAMBIOS_POR_HILO):
        # Generar índices aleatorios
        index1 = random.randint(0, NUMERO_ELEMENTOS - 1)
        index2 = random.randint(0, NUMERO_ELEMENTOS - 1)
        
        # Intercambio controlado con lock para evitar inconsistencias
        with lock:
            lista1[index1], lista2[index2] = lista2[index2], lista1[index1]

# Crear e iniciar los hilos para rellenar las listas
hilo_par = threading.Thread(target=insertar_numeros, args=(lista1, "par"))
hilo_impar = threading.Thread(target=insertar_numeros, args=(lista2, "impar"))
hilo_par.start()
hilo_impar.start()
hilo_par.join()
hilo_impar.join()

# Crear e iniciar los hilos para intercambiar elementos entre listas
hilos_intercambio = []
for _ in range(NUMERO_HILOS_INTERCAMBIO):
    hilo = threading.Thread(target=intercambiar_elementos)
    hilos_intercambio.append(hilo)
    hilo.start()

# Esperar a que todos los hilos de intercambio terminen
for hilo in hilos_intercambio:
    hilo.join()

# Calcular las sumas finales
suma_lista1 = sum(lista1)
suma_lista2 = sum(lista2)
suma_total = suma_lista1 + suma_lista2

print(f"Suma de lista1: {suma_lista1}")
print(f"Suma de lista2: {suma_lista2}")
print(f"Suma total: {suma_total}")
