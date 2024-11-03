# file_path: Percorso del file da cui leggere i magic bytes. 
# # num_bytes: Numero di byte da leggere all'inizio del file (default: 8). 
def get_magic_bytes(file_path, num_bytes=8): 
    try: 
        with open(file_path, 'rb') as f: # apertura dei file in modalità binaria 
            magic_bytes = f.read(num_bytes) 
            return magic_bytes 
    except IOError as e: print(f"Errore nell'apertura del file: {e}") 
    return None 
if __name__ == "__main__": file_path = input("Inserisci il percorso del file: ") 
magic_bytes = get_magic_bytes(file_path) 
if magic_bytes: print("Magic bytes:", ' '.join(f'{byte:02X}' for byte in magic_bytes))