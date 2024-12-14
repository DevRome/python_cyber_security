# creazione di un indirizzo IP con destinazione indirizzo specifco
from scapy.all import IP, ICMP, send

# creo un pacchetto IP con ICMP diretto ad un host specifico
packet = IP(dst="192.168.1.1") / ICMP()

# invio del pacchetto
try:
    # invio di 10 pacchetto ogni 1 secondi
    send(packet, count=10, inter=1)
except Exception as e:
    print(f"Errore: {e}")
