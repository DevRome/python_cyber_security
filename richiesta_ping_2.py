from scapy.all import ICMP, IP, srl

# creazione di un pacchetto ICMP destinatario a una rete
ip = IP(dst = Net("192.168.1.0/24")) # creo istanza IP
icmp = ICMP()
packet = ip/icmp

send(packet)