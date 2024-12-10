import requests # ci permette di inviare richieste HTTP usando python
# metodi: get, post, put, delete, patch, put, head
# request restituisce un Response Object con data (content, encoding, status ecc.)

def get_mac_vendor(mac_address): 
    url = f"https://api.macvendors.com/{mac_address}" 
    try: 
        response = requests.get(url) 
        response.raise_for_status() # Solleva un errore per risposte non-successo 
        return response.text # Il nome del produttore viene restituito come testo 
    except requests.RequestException as e: 
        return f"Errore durante la richiesta: {e}" 

# Esempio di utilizzo della funzione 
mac_address = input("Inserisci un indirizzo MAC (es. AA:BB:CC:DD:EE:FF): ") 
vendor = get_mac_vendor(mac_address) 
print(f"Il produttore della scheda di rete per l'indirizzo MAC {mac_address} è: {vendor}")