from smartcard.System import readers
from smartcard.Exceptions import NoCardException
import time


def get_card_uid():

    try:

        # Nouvelle recherche lecteur à chaque appel
        liste = readers()

        if not liste:
            return None


        reader = liste[0]


        connection = reader.createConnection()


        try:
            connection.connect()

        except Exception:

            # petite attente puis nouvelle tentative
            time.sleep(0.2)

            connection = reader.createConnection()
            connection.connect()



        command = [
            0xFF,
            0xCA,
            0x00,
            0x00,
            0x00
        ]


        data, sw1, sw2 = connection.transmit(
            command
        )


        if sw1 == 0x90 and data:

            uid = ":".join(
                f"{x:02X}"
                for x in data
            )

            return uid



    except NoCardException:

        return None



    except Exception as e:

        print(
            "Erreur NFC:",
            e
        )

        return None



    return None