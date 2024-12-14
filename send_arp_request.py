from scapy import *

arp_request = ARP(pdst="192.168.1.1")

send(arp_request)