from scapy.all import sniff, TCP, IP 
from collections import defaultdict 
import time # Contatore per le richieste SYN per ogni IP 
syn_counters = defaultdict(int) #Un dizionario che tiene traccia del numero di pacchetti SYN inviati da ciascun indirizzo IP sorgente. 
RESET_INTERVAL = 10 # Intervallo di tempo per resettare i contatori (in secondi) 
SYN_THRESHOLD = 100 # Soglia di SYN per considerare il traffico sospetto da un singolo IP che, se superata, può indicare un attacco SYN flood.

#Resetta i contatori dei pacchetti SYN per ciascun IP e stampa un messaggio che indica il reset dei contatori. Questo aiuta a prevenire il conteggio di pacchetti SYN vecchi che potrebbero non essere più rilevanti. 
def reset_counters(): 
    global syn_counters 
    syn_counters = defaultdict(int) 
    print("Counters reset.")

# Questa funzione viene chiamata per ogni pacchetto TCP intercettato. Controlla se il pacchetto è un pacchetto SYN (un pacchetto TCP con solo il flag SYN impostato, indicando un tentativo di iniziare una connessione). Se lo è, incrementa il contatore per l'indirizzo IP sorgente di quel pacchetto. Se il numero di pacchetti SYN da un singolo IP supera la soglia, viene segnalato un possibile attacco SYN flood. 
def syn_flood(pkt): 
    if TCP in pkt and pkt[TCP].flags == 'S': 
        src_ip = pkt[IP].src 
        syn_counters[src_ip] += 1 # Controlla se le richieste SYN superano la soglia 
        if syn_counters[src_ip] > SYN_THRESHOLD: print(f"Possible SYN flood attack detected from {src_ip}!")

#Questa è la funzione principale che coordina lo sniffing dei pacchetti e il reset dei contatori. Utilizza la funzione sniff di Scapy per catturare pacchetti TCP e li elabora utilizzando la funzione syn_flood. Il reset_timer assicura che i contatori vengano resettati all'intervallo specificato. 
def main(): reset_timer = time.time() + RESET_INTERVAL 
while True: # Avvia lo sniffing dei pacchetti 
    sniff(filter="tcp", prn=syn_flood, store=0, count=10) # Resetta i contatori a intervalli regolari 
    if time.time() > reset_timer: 
        reset_counters() 
        reset_timer = time.time() + RESET_INTERVAL