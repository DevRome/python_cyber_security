import dns.resolver 

def resolve_dns(domain): 
    print(f"Risultati DNS per il dominio: {domain}\n") 
    
    # Risolvi il record A 
    try: 
        a_records = dns.resolver.resolve(domain, 'A') 
        print("Record A (IPv4):") 
        for record in a_records: print(record.address) 
    except Exception as e: print(f"Errore risolvendo il Record A: {e}") 
    
    print("\n") # Aggiungi una linea vuota tra i risultati
    
    # Risolvi il record MX 
    try: 
        mx_records = dns.resolver.resolve(domain, 'MX') 
        print("Record MX (Mail Exchange):") 
        for record in mx_records: print(f"Priority: {record.preference}, Mail Server: {record.exchange}") 
    except Exception as e: print(f"Errore risolvendo il Record MX: {e}") 
    
    print("\n") # Aggiungi una linea vuota tra i risultati

    # Risolvi il record NS 
    try: 
        ns_records = dns.resolver.resolve(domain, 'NS') 
        print("Record NS (Name Server):") 
        for record in ns_records: print(record.target) 
    except Exception as e: print(f"Errore risolvendo il Record NS: {e}") 

resolve_dns("example.com")