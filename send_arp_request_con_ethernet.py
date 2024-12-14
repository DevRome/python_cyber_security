from scapy import *

ethernet_frame = Ether(dst="ff:ff:ff:ff:ff:ff")

arp_request = ARP(pdst="192.168.1.1")

packet = ethernet_frame / arp_request

try:
    send(packet, iface="eth0")
    print("Pacchetto ARP inviato correttamente")
except Exception as e:
    print(f"Errore durante l'invio delmpacchetto: {e}")