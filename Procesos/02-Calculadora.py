import subprocess
import pyautogui
import time

# Abre la calculadora de Windows
subprocess.Popen('calc.exe')

# Espera un par de segundos para asegurarse que esté abierta
time.sleep(2)

# Escribe un número
pyautogui.write('1234')
