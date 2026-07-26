from smartcard.System import readers
from smartcard.util import toHexString


# Liste des lecteurs NFC
r = readers()

if len(r) == 0:
    print("Aucun lecteur NFC trouvé")
    exit()


reader = r[0]

print("Lecteur :", reader)


# Connexion au lecteur
connection = reader.createConnection()
connection.connect()


# Commande APDU Get UID
command = [
    0xFF,
    0xCA,
    0x00,
    0x00,
    0x00
]


data, sw1, sw2 = connection.transmit(command)


print("Réponse brute :", data)
print("Status :", hex(sw1), hex(sw2))


if sw1 == 0x90 and sw2 == 0x00:
    uid = toHexString(data)
    print("UID NFC :", uid)

else:
    print("Impossible de lire l'UID")