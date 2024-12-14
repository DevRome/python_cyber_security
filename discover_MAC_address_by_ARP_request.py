from scapy.all import Ether, ARP, srp 
# Definisci l'indirizzo IP target 
ip_target = "192.168.1.1" 
# Crea un pacchetto ARP 
arp_request = ARP(pdst=ip_target) 
# Invia la richiesta ARP nella rete e attendi la risposta 
result, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_request, timeout=2, iface="eth0", verbose=False) 
# Analizza e stampa la risposta 
for sent, received in result: print(f"L'indirizzo MAC di {ip_target} è {received.hwsrc}") 
