# creazione di un indirizzo IP con destinazione indirizzo specifico
from scapy.all import *

# creazione di un pacchetto ICMP destinato ad una rete
ip = IP(dst=Net("192.168.1.0/24"))
icmp = ICMP()
packet = ip/icmp

# invio del pacchetto a tutti gli indirizzi della subnet
try: send(packet)
except Exception as e: print(f"Errore: {e}")