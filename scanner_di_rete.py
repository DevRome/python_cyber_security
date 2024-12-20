from scapy.all import *
broadcast = "FF:FF:FF:FF:FF:FF"
ether_layer = Ether(dst=broadcast)
ip_range = "192.168.1.1/24"
arp_layer = ARP(pdst=ip_range)

packet = ether_layer / arp_layer
ans, unans = srp(packet, iface="eth0", timeout=2)

for snd, rcv in ans:
    ip = rcv[ARP].psrc
    mac = rcv[Ether].src
    print("IP = ", ip, "MAC = ", mac)