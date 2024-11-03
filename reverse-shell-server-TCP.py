import socket 
SERVER_HOST = "0.0.0.0"
# Imposta l'indirizzo IP del server . Indica che il server è raggiungibile su tutte le interfacce di rete del dispositivo. In pratica, il server ascolta su tutti gli indirizzi IP della macchina. 
SERVER_PORT = 5003 
# Questa è la porta sulla quale il server sta ascoltando. Le connessioni in entrata su questa porta saranno accettate dal server. 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#Crea un socket TCP/IP. l'uso di IPv4, indica l'uso di TCP, che è orientato alla connessione. 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# Questa opzione permette al socket di riutilizzare l'indirizzo IP e la porta, utile in caso di riavvio rapido del server. 
server_socket.bind((SERVER_HOST, SERVER_PORT)) 
# Associa il server all'indirizzo HOST e alla porta specificati. server_socket.listen(1) 
# Mette il server in ascolto, permettendo una connessione in attesa alla volta. 
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...") 
client_socket, client_address = server_socket.accept() 
# Accetta una connessione dal client che si connette e restituisce un nuovo socket per quel client insieme all’indirizzo del client 
print(f"{client_address[0]}:{client_address[1]} Connected!") 

while True: # Ricevi il comando dal server ll server attende che l'utente (l'operatore del server) inserisca un comando tramite la funzione input() 
    command = input("Enter the command you want to execute:") 
    client_socket.send(command.encode()) 
    # Invia il comando codificato in bytes al client 
    if command.lower() == "exit": 
    # Se il comando inserito è "exit", il ciclo si interrompe e il server termina la connessione. 
        break 
    results = client_socket.recv(1024).decode() # Attende la risposta dal client, ricevendo fino a 1024 byte e decodificandoli per convertirli in stringa. print(results) 
    client_socket.close() # Chiude la connessione con il client. 
    server_socket.close() # Chiude il socket del server, terminando l'abilità di accettare ulteriori connessioni