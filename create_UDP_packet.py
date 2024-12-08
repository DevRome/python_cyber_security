# Scrivere un programma che crea un pacchetto UDP; 
from scapy.all import IP, UDP 

# Crea un pacchetto IP destinato a un host specifico 
ip = IP(dst="192.168.1.24") 

# Aggiungi un layer UDP al pacchetto IP 
udp = UDP(sport=12345, dport=80) 

# Combinare i layer IP e UDP 
packet = ip/udp 

# Visualizza i dettagli del pacchetto 
packet.show()