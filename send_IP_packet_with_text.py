from scapy.all import IP, TCP, Raw, send


def create_and_send_packet(dst_ip, dst_port, message):

    # crea un pacchetto IP con il destinatario specificato
    ip_layer = IP(dst=dst_ip)

    # crea un pacchetto TCP sulla porta destinataria
    tcp_layer = TCP(dport=dst_port)

    # prepara il payload, che è il messaggio da inviare
    payload = Raw(load=message.encode("utf-8"))

    # combina i layer per formare il pacchetto completo
    packet = ip_layer / tcp_layer / payload

    # invia il pacchetto
    try:
        send(packet, verbose=True)
    except Exception as e:
        print("Errore durante l'invio del pacchetto:", e)

# configura indirizzi IP e porta destinatari, ed il messaggio testo
destination_ip = "127.0.0.1" # ip server destinatario
destination_port = 12345 # porta tcp del server
message = "Ciao" # messaggio da inviare

# chiama la funzione per creare ed inviare il pacchetto
create_and_send_packet(destination_ip, destination_port, message)

