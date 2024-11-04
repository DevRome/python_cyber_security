# programma per ottenere MAC address

import uuid

macAddress = hex(uuid.getnode())
print(macAddress)

# formattata bene (fatta da me)
newString = ""
couple = ""
for chars in range(0, len(macAddress), 2):
    couple = macAddress[chars] + macAddress[chars+1] + "."
    newString += couple
print(newString[3:-1])