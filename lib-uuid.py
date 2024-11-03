import uuid

def get_mac_address():
    mac = uuid.getnode()
    print("L'indirizzo MAC decimale della macchina è: ", mac)

    # converte l'indirizzo MAC da un valore decimale a una stringa esadicimale formattata
    mac_address = ':'.join([f"{(mac >> elements) & 0xff:02x}" for elements in range(40, -1, -8)])

    return mac_address

print("L'indirizzo esadecimale MAC della macchina è: ", get_mac_address())