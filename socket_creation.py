# Lato Server TCP 
import socket 
def start_server(): 
    # Crea una socket TCP 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Associa la socket a un indirizzo IP e una porta 
    server_socket.bind(('localhost', 12345))
    
    # Metti la socket in modalità di ascolto 
    server_socket.listen(1) 
    print("Server in ascolto su localhost:12345") 
    
    # Accetta una connessione 
    connection, client_address = server_socket.accept() 
    print(f"Connessione da {client_address}") 
    
    try: 
        while True: # Ricevi i dati inviati dal client 
            data = connection.recv(1024) 
            print(f"Ricevuto: {data.decode()}") 
            if data: # Invia indietro i dati ricevuti (echo) 
                connection.sendall(data) 
            else: # Nessun dato ricevuto, chiudi la connessione 
                print("Nessun dato ricevuto. Chiusura connessione.") 
                break 
    finally: # Chiudi la connessione 
        connection.close() 

start_server()


# Lato Client TCP
import socket 
def start_client(): 
    
    # Crea una socket TCP 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Connettiti al server 
    server_address = ('localhost', 12345) 
    client_socket.connect(server_address) 
    
    try: # Invia dati al server 
        message = 'Ciao, Server!' 
        print(f"Inviando: {message}") 
        client_socket.sendall(message.encode()) 
        
        # Ricevi la risposta dal server 
        response = client_socket.recv(1024) 
        
        print(f"Ricevuto: {response.decode()}") 
    finally: # Chiudi la socket 
        client_socket.close() 

start_client()