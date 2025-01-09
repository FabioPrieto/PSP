from threading import Thread
import subprocess

def hacer_ping(ip, resultados):
    resultado = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, text=True)
    with open("resultados_ping.txt", "a") as f:
        f.write(f"{ip}: {'Exitoso' if resultado.returncode == 0 else 'Fallido'}\n")

hilos = []
for i in range(1, 256):
    ip = f"10.10.30.{i}"
    hilo = Thread(target=hacer_ping, args=(ip,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Pings completados. Resultados en 'resultados_ping.txt'")

