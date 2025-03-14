import socket
from tkinter import *
import threading
import time

def conectarServidor():
  global client
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((SERVER, PORT))
  lblInfo["text"]= client.recv(1024).decode()
  
def inscribir ():
  global client
  client.sendall(bytes("#INSCRIBIR#"+entNombre.get() +"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()

def enviarJugada(jugada):  
  global client
  client.sendall(bytes("#JUGADA#"+jugada+"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode() 
  
def consultaPuntos():
  global client
  client.sendall(bytes("#PUNTUACION#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()    
  
def resultadoJugada(numJ):
    def reintentar():
        global client
        while True:
            client.sendall(bytes("#RESULTADOJUGADA#" + numJ + "#", 'UTF-8'))
            respuesta = client.recv(1024).decode()
            if respuesta.startswith("#OK#"):
                lblInfo["text"] = respuesta
                break
            elif respuesta.startswith("#NOK#"):
                lblInfo["text"] = f"Jugando: {respuesta} Reintentando en 5 segundos..."
                time.sleep(5)  # Espera de 5 segundos antes de reintentar
            else:
                lblInfo["text"] = f"Respuesta inesperada: {respuesta}"
                break

    # Inicia un hilo para realizar las solicitudes en segundo plano
    hilo = threading.Thread(target=reintentar, daemon=True)
    hilo.start()  
  
#if __name__ == '__main__':
SERVER = "127.0.0.1"
PORT = 2000
client = None
informacion =""
fPPT = Tk() 
fPPT.title("Piedra-Papel-Tijera")
fPPT.geometry("300x300")
fPPT.resizable(True, True)
lblInfo = Label(fPPT, text=informacion)
lblInfo.place(x=0,y=230)
btnConn = Button(fPPT, text = 'Conectar', command = conectarServidor)
btnConn.place(x = 150,y = 50)
entNombre = Entry(fPPT)
entNombre.place(x = 20,y=100)
btnInscribir = Button(fPPT, text = 'Inscribir', command = inscribir)
btnInscribir.place(x = 150,y = 100)
btnPiedra = Button(fPPT, text = 'piedra', command = lambda: enviarJugada("piedra"))
btnPiedra.place(x = 50,y = 150)
btnPapel = Button(fPPT, text = 'papel', command = lambda: enviarJugada("papel"))
btnPapel.place(x = 100,y = 150)
btnTijera = Button(fPPT, text = 'tijera', command = lambda: enviarJugada("tijera"))
btnTijera.place(x = 150,y = 150)
spnNumJugada = Spinbox(fPPT, from_=1, to=99,increment=1)
spnNumJugada.place(x = 30,y=200, width=50)
btnResultado = Button(fPPT, text = 'Resultado', command = lambda: resultadoJugada(spnNumJugada.get()))
btnResultado.place(x = 80,y = 200)
btnPuntos = Button(fPPT, text = 'Puntuación', command =consultaPuntos)
btnPuntos.place(x = 150,y = 200)
fPPT.mainloop()