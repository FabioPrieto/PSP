import socket

HOST = ""
PORT = 2000
try:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        s.accept()
        conn, addr = s.accept()
        with conn:
            print(f"conexion exitosa del cliente. IP {addr[0]}, Puerto {addr[1]}")
            while True:
                data = conn.recv(1024)
                print(data)
                if data ==b"0":
                    break
                conn.sendall(b"mensaje recibido") 
except socket.error as e:
    print("Error en socket: %s" %e)
    