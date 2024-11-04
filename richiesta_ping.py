from scapy.all import ICMP, IP, sr

src_ip="192.168.33.99"
dest_ip="www.prova.it" # indirizzo obiettivo
ip_layer = IP(src=src_ip, dst=dest_ip) # creo istanza IP

print(ip_layer.show())