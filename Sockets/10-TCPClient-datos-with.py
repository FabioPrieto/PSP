import socket

HOST = "127.0.0.1"
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT)) #Bloqueante
    print("Conexión con éxito")
    s.send(b"Yo, tu cliente, te saludo.")
    data = s.recv #Línea bloqueante

print("recibido: ", repr(data))