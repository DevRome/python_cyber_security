from scapy.all import *

# creazione di un pacchetto IP con il flag Don't Fragment impostato
packet = IP(dst="192.168.1.1", flags="DF")

# visualizzazione dell'intestazione del pacchetto
packet.show()