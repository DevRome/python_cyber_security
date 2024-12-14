from scapy.all import Ether, ARP, srp 
# Definisci la subnet 
subnet = "192.168.1.0/24" 
# Crea un pacchetto ARP per la subnet 
arp_request = ARP(pdst=subnet) 
# Invia la richiesta ARP nella rete 
result, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_request, timeout=2, iface="eth0", verbose=False) 
# Analizza e stampa gli indirizzi MAC dei dispositivi attivi 
print("Dispositivi attivi nella subnet:")
for sent, received in result: print(f"IP: {received.psrc}, MAC: {received.hwsrc}")