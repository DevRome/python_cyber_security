# Programma Python che determina indirizzo IP locale, usando la libreira socket e le istruzioni gethostname() e gethostbyname()

import socket

# recupero l'host name locale
myHostName = socket.gethostname()

# recupero l'indirizzo IP del localhost
myIP = socket.gethostbyname(myHostName)

# stampo informazioni
print(f"Il nome dell'host: {myHostName};\nl'indirizzo IP privato: {myIP} ")