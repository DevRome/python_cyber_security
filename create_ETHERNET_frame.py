from scapy.all import Ether, IP, ICMP, send

# creazione di un frame Ethernet con indirizzi MAC specifici
ethernet_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:01:02:02:01:00")

# creazione di un pacchetto IP con un messaggio ICMP (ping)
ip_packet = IP(dst="192.168.1.1")/ICMP()

# combina il frame Ethernet con il pacchetto IP
packet = ethernet_frame / ip_packet

# visulizza la struttura del pacchetto
packet.show()

# invia il pacchetto
send(packet)