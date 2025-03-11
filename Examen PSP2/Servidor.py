import socket
import threading
import time

jugadores = []

class Jugador: 
  def __init__(self): 
    self._nick = "" #nombre del jugador
    self._addr = "" #ip del jugador
  
  @property
  def nick(self): 
    return self._nick 
  
  @property
  def addr(self): 
    return self._addr 
  
  @nick.setter 
  def nick(self, nombre): 
    self._nick = nombre 

  @addr.setter 
  def addr(self, addr): 
    self._addr = addr 



            
class ManejoCliente(threading.Thread):
  def __init__(self,clientAddress,clientsocket):
    threading.Thread.__init__(self)
    self.csocket = clientsocket
    self.cAddress = clientAddress
    print ("Cliente conectado desde: ", self.cAddress)
    jugador = Jugador()
    
  def run(self):
    print ("Escuchando a peticiones de cliente: ", self.cAddress)
    #mensaje de bienvenida con el protocolo
    bienvenida ="#ON#nickname#\n#OFF#nickname#\n#LIST#"
    self.csocket.send(bytes(bienvenida,'UTF-8'))  
    
    while True:
      data = self.csocket.recv(512).decode("utf_8")
      print ("Enviado desde cliente:<",data,">")      
      subdatos =  data.split("#")
      respuesta="#OK#"
      if subdatos[1] == "ON":
        if jugador._nick =="":
          jugador.nick = subdatos[2]
          jugador.addr = self.cAddress
          jugadores.append(jugador)
        else:
          respuesta="#NOK#jugadore ya tiene nick#"
      elif subdatos[1] == "OFF":
        #comprobra valor válido
        for juagador in jugadores:
          if juagador._nick == subdatos[2]:
            ecxiste = True
            eliminar = juagador
        if (self.cAddress == jugadores[0]._addr or self.cAddress == eliminar._addr) and ecxiste:
          jugadores.remove(eliminar)
          del eliminar
          respuesta="#OK#jugador eliminado#"
        else:
          respuesta="#NOK#jugador no existente o no jugador super#"
      elif subdatos[1] == "LIST":
        respuesta = "#OK#\n"
        for juagador in jugadores:
          respuesta += f"#{juagador._nick}#{juagador._addr}#\n"

      self.csocket.send(bytes(respuesta,'UTF-8'))  
      
if __name__ == '__main__':
  HOST = ""
  PORT = 2000
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((HOST, PORT))
  print("Servidor iniciado. Esperando clientes...")
  while True:
    server.listen()
    jugador = Jugador()
    clientsock, clientAddress = server.accept()
    t = ManejoCliente(clientAddress, clientsock)
    t.start()