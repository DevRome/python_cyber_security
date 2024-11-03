import hashlib 

def calculate_sha256(file_path): 
    """Calcola l'hash SHA‐256 di un file specificato dal percorso file_path.""" 
    sha256_hash = hashlib.sha256() # Apriamo il file in modalità binaria per la lettura 
    with open(file_path, "rb") as f: # Leggiamo il file a blocchi per evitare l'uso eccessivo della memoria con file grandi EVITARE DI SOVRACCARICARE MEMORIA 
        for byte_block in iter(lambda: f.read(4096), b""): sha256_hash.update(byte_block) # Ritorniamo l'hash in formato esadecimale 
        return sha256_hash.hexdigest() # Esempio di utilizzo della funzione 
    
file_path = 'prova.txt' 
checksum = calculate_sha256(file_path) 
print(f"SHA‐256 checksum del file è: {checksum}")