import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #bloqueante
    print ("Conexión con éxito")
    
    while True:
        mensaje = input("Escribe un mensaje para enviar al servidor ('en blanco' para terminar): ")
        if mensaje == "":
            s.send(b'0')
        else: 
            s.send(b'%s' % mensaje.encode())  
        
        data = s.recv(1024) #línea bloqueante
        print ('recibido: ', repr(data))
        