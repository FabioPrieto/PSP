import socket
import random

IP = ""
PORT = 2000
adivinar = random.randrange(1,9)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP,PORT))
    s.listen()
    
    print("Servidor escuchando")
    print(f"número a adivinar: {adivinar}")
    
    (cli,addr) = s.accept() #bloqueante
    print(f"Cliente conectado en: {addr}")
    
    cli.send(b"intenta adivinar mi numero!")
    while True:
        dato = cli.recv(64).decode()
        print(dato)
        if int(dato) == adivinar:
            cli.send(b"HAS ACERTADO")
            break
        elif int(dato) > adivinar:
            cli.send(b"Numero Menor")
        else:
            cli.send(b"Numero Mayor")

    cli.close
