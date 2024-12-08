from scapy.all import *

source_ip = "192.168.33.99"
destination_ip = "8.8.8.8" # indirizzo obiettivo
ip_layer = IP(src=source_ip, dst=destination_ip) # creo istanza IP

print(ip_layer.show())

# creiamo una istanza ICMP (Internet Control Message Protocol)
# id=100 aiuta il protocollo a tracciare i pacchetti
# ovvero le diverse sequenze di ICMP
icmp_req = ICMP(id=100)

# combiniamo i livelli:
packet = ip_layer / icmp_req

# per inviare la request usiamo la funz. sr()
response = sr(packet, ifaces="eth0")
if response: response.show()