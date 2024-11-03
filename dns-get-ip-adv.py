import dns.resolver

def resolve_host_advanced(hostname):
    try:
        answers = dns.resolver.resolve(hostname, 'A') 
        # 'A' per i record IPv4
        # answers è un oggetto contenente tutti i record A trovati ovvero indirizzi IP trovati
        for answer in answers:
            print(f"L'indirizzo IP di {hostname} è {answer}")
    
    # eccezione solevata quando il DNS risponde ma non fornisce record del tipo richiesto
    except dns.resolver.NoAnswer as error:
        print(f"Nessuna risposta dal DNS per {hostname}: {error}")

    # eccezione sollevta quando uk nime di dominio non esiste nel DNS
    except dns.resolver.NXDOMAIN as error:
        print(f"Nome dominio {hostname} non esistente: {error}")

    except Exception as error:
        print(f"Errore nella risoluzione di {hostname}: {error}")

hostname = "www.unimarconi.it"
resolve_host_advanced(hostname)      
