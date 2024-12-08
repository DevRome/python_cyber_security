from scapy.all import *

# indirizzo IP destinazione e porta
destionation_ip = "192.168.0.1"
destination_port = 80

# creazione del pacchetto IP
ip_layer = IP(dst=destionation_ip)

# creazione segment TCP con il flag SYN (inizio connessione TCP)
syn_segment = TCP(dport=destination_port, flags="S")

# invio del segment SYN
response = send(ip_layer/syn_segment)

# creazione segment TCP con il flag RST (reset della connessione)
rst_segment = TCP(dport=destination_port, flags="R")

# invio del segment RST per terminare la connessione
send(ip_layer/rst_segment)