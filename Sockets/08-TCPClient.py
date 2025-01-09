import socket

HOST = "127.0.0.1"
PORT = 3000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))
except socket.error as exc:
    print("excepcion de socket: "+ exc)

finally:
    s.close