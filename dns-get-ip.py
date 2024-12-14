import socket
# socket è un modulo che è un'interfaccia per la rete a basso livello fornito da Python

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Indirizzo IP per {hostname}: {ip_address}")
    except socket.gaierror as e:
        print(f"Errore nella risoluzione dui {hostname}: {e}")

resolve_hostname("www.casa-alessandra.it")