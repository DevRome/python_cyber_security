from scapy.all import *

# creazione del pacchetto IP
ip = IP(dst="192.168.0.1")

# creazione di un pacchetto TCP
tcp = TCP(sport=12345, dport=80, flags="S", seq=1000)

# combinazione dei pacchetti IP e TCP
packet = ip/tcp

# visualizza il pacchetto
packet.show()