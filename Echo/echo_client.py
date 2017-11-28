import sys
import socket

    # Creo il socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tento la connessione al server
try:
    socket.connect(("127.0.0.1", 3000))
except OSError as err:  # Gestisco errori di connessione
    print(err)
    sys.exit()

    # Ricevo la stringa di avvenuta connessione dal server
welcome = socket.recv(128).decode()
print(welcome)

while (1):
        # Invio una stringa, convertendola a sequenza di byte 
    msg = input("> ")
    socket.send(msg.encode())

    if (msg == "exit"):
        break
    
        # Ricevo una una sequenza di byte, convertendola a stringa
    response = socket.recv(32).decode()
    print("response: ",response)


goodbye = socket.recv(128).decode()
print(goodbye)

    # Chiudo il socket
socket.close()
