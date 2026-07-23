import pystray
from PIL import Image
import os
import threading
import time


icon = None


def quit_app(icon, item):
    icon.stop()



def create_tray():

    global icon


    dossier = os.path.dirname(
        os.path.abspath(__file__)
    )


    chemin_icone = os.path.join(
        dossier,
        "icon.ico"
    )


    with open(
        os.path.join(dossier, "tray.log"),
        "a",
        encoding="utf-8"
    ) as f:
        f.write(
            "Démarrage tray\n"
        )
        f.write(
            chemin_icone + "\n"
        )


    if not os.path.exists(chemin_icone):

        with open(
            os.path.join(dossier, "tray.log"),
            "a"
        ) as f:
            f.write(
                "ICON ABSENTE\n"
            )

        return


    image = Image.open(
        chemin_icone
    )


    menu = pystray.Menu(

        pystray.MenuItem(
            "NFCGuard actif",
            lambda: None
        ),

        pystray.MenuItem(
            "Quitter",
            quit_app
        )
    )


    icon = pystray.Icon(

        "NFCGuard",

        image,

        "NFCGuard",

        menu

    )


    with open(
        os.path.join(dossier, "tray.log"),
        "a"
    ) as f:
        f.write(
            "Icon run\n"
        )


    icon.run()



def start_tray():

    thread = threading.Thread(

        target=create_tray,

        daemon=False

    )


    thread.start()