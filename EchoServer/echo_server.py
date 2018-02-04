import sys
import socket

    # Creo il serversocket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server creato")

    # Collego serversocket a host e porta
try:
    serversocket.bind(("127.0.0.1", 3000))
except (socket.error, msg): # Gestisco casi in cui la porta gia esiste
    print(msg)
    serversocket.close()
    sys.exit()

print("Server avviato su 127.0.0.1:3000")

    # Imposto il server in ascolto
serversocket.listen()
print("Server in ascolto..")

    # Attendo una connessione entrante
(connection, address) = serversocket.accept()

    # Invio una stringa, convertendola a sequenza di byte
connection.send('Benvenuto! Inviami un messaggio e io ti rispondero. Per chiudere la connessione inviami \'exit\''.encode())
 
while (1):
        # Ricevo una sequenza di byte e converto a stringa
    input = connection.recv(32).decode()
    if (input == "exit"):    # Controllo se è il segnale di chiusura del server
        break
    print("incoming: ", input)
        # Rispondo con lo stesso messaggio
    connection.send(input.encode())
    print("outgoing: ", input)


saluto = "Arrivederci! Server in chiusura.."
connection.send(saluto.encode())
print(saluto)

    # Chiudo il serversocket
serversocket.close()
print("Server chiuso")
