from scapy.all import *

# la classe ip consente di creare pacchetti IP
destination_ip = "192.16.1.15"

ip_layer = IP(dst=destination_ip)

print(ip_layer.version)
print(ip_layer.len)
print(ip_layer.dst)