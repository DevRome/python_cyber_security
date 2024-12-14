# creazione di un indirizzo IP con destinazione indirizzo specifco
from scapy.all import IP, ICMP, send

# creo un pacchetto Ethernet che incapsula IP con ICMP diretto ad un host specifico
packet = Ether()/IP(dst="192.168.1.1") / ICMP()

# invio del pacchetto
try:
    # invio di 10 pacchetto ogni 1 secondi
    send(packet)
except Exception as e:
    print(f"Errore: {e}")
