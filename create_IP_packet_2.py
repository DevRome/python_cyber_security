from scapy.all import *

# creazione di un pacchetto IP con destinazione un indirizzo specifico
packet = IP(dst="192.168.1.1") / ICMP()

# invio del pacchetto
send(packet)