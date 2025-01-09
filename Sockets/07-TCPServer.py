import socket

HOST = "127.0.0.1" #dirección de loopback standart para localhost
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 - TCP
try:
    s.bind((HOST,PORT))
    s.listen(1) #creo una lista de un cliente en epera
    conn, addr = s.accept()
    print(f"conexion exitosa del cliente. IP {addr[0]}, Puerto {addr[1]}")
except socket.error as exc:
    print("Excepción de socket: %s" % exc)
finally:
    #Cerramos servidor
    s.close()