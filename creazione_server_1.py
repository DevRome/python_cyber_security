# creazione Server
import socket

def create_server():

    # creo una istanza del socke TCP/IP
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # associo il scoket creato a un indirizzo pubblico ed una porta X=12900
    port = 12900
    server_address = ('localhost', port)

    # stampo info in console
    print(f"il server si sta attivando su:{server_address[0]}, porta:{server_address[1]}")

    # binding
    serversocket.bind(server_address)

    # mettiamo il socket in modalità di ascaloto dove 10 è il backlog num maxdi connessioni pendenti che il sistema mette in coda.
    # Se il server è temporaneamente troppo occupato per accettare nuove connessioni, esso può mettere in coda fino a 10 connessioni.
    # Ogni tentativo di connessione oltre questo limite potrebbe essere rifiutato. QUesta funzionalità è importante per controlare come un server TCP gestisce il traffico in entrata, specialemnte sotto carichi di lavoro elevati o attacchi DDoS

    # loop infinito consente al server di rimanere in esecuzione ed accettare connessioni multiple una dopo l'altra
    while True:
        print("In attesa di una nuova connessione")
        
        # Asoetta una connessione in entrata; blocca l'esecuzione del server finché una connessione non viene stabilita. Quando un client si connette, accept() ritorna di nuovo socket connection dedicato alla comunicazioe con quel client e l'indirizzo client_adddress del client
        connection, client_address = serversocket.accept()

        try:
            print(f"Connessione da {client_address}")

            # ricevi ati in piccole porzioni e inviali indietro. gestisce la ricezione e l'invio dei dati per quella specifica connessione
            while True:

                # riceve dati dal client, il numero 16 specifica il numero massimo di byte da leggere alla volta
                data = connection.recv(16)
                print(f"ricevuto: {data.decode()}")
                if data:
                    print("Invio dati al client")
                    connection.sendall(data)

                # se non vengono ricevuti dati (cioè data è vuoto) significa che il client ha chiuso la connessione    
                else:
                    print("nessun dato ricevuto dal client")
                    break
        finally:
            connection.close()


create_server() 