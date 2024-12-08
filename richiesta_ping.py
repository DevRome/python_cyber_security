from scapy.all import ICMP, IP, sr


src_ip="192.168.33.99"
dest_ip="8.8.8.8" # indirizzo obiettivo
ip_layer = IP(src=src_ip, dst=dest_ip) # creo istanza IP

try:
    print(ip_layer.show())
except Exception as e:
    print(f"Errore: {e}")