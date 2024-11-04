# creazione di un indirizzo IP con destinazione indirizzo specifco
from scapy.all import IP, ICMP, send

packet = IP(dst="192.168.1.1") / ICMP()

# invio del pacchetto
send(packet)
