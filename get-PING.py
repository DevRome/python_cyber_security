import subprocess 

def ping_host(): 
    
    # input utente
    host = input("Inserisci l'indirizzo IP o il dominio da pingare: ") 
    
    try: # Esegue il comando ping (modifica -c 4 a /n 4 su Windows) 
        result = subprocess.run(["ping", "-c", "4", host], text=True, capture_output=True) 
        # Stampa l'output del comando 
        print("Output del comando ping:") 
        print(result.stdout) 
    
    except FileNotFoundError: # Errore se il comando ping non è trovato 
        print("Comando ping non trovato nel sistema.") 
    
    except Exception as e: # Altri errori generici 
        print(f"Si è verificato un errore: {e}") 

# Esegui la funzione 
ping_host()