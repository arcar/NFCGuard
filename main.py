import tkinter as tk
import ctypes
import os

from PIL import Image, ImageTk

from config import AUTHORIZED_UID, TIMEOUT, LOGO
from nfc_reader import get_card_uid
from tray import start_tray


# ==========================
# Etats globaux
# ==========================

screen_active = False
badge_lost = False



# ==========================
# Verrouillage Windows
# ==========================

def lock_windows():

    print("VERROUILLAGE WINDOWS")

    ctypes.windll.user32.LockWorkStation()



# ==========================
# Lecture badge
# ==========================

def get_uid():

    uid = get_card_uid()

    print(
        "UID détecté :",
        uid
    )

    return uid



def badge_present():

    return get_uid() == AUTHORIZED_UID



# ==========================
# Fenêtre sécurité
# ==========================

def show_badge_screen():

    global screen_active

    if screen_active:
        return


    screen_active = True


    win = tk.Toplevel()

    win.attributes(
        "-fullscreen",
        True
    )

    win.attributes(
        "-topmost",
        True
    )

    win.configure(
        bg="black"
    )


    win.protocol(
        "WM_DELETE_WINDOW",
        lambda: None
    )


    # ----------------------
    # Logo
    # ----------------------

    if os.path.exists(LOGO):

        try:

            image = Image.open(LOGO)

            image.thumbnail(
                (300,300)
            )


            logo_img = ImageTk.PhotoImage(
                image
            )


            logo = tk.Label(
                win,
                image=logo_img,
                bg="black"
            )


            logo.image = logo_img


            logo.pack(
                pady=50
            )


        except Exception as e:

            print(
                "Erreur logo :",
                e
            )



    # ----------------------
    # Texte
    # ----------------------

    message = tk.Label(

        win,

        text="Présentez votre badge NFC",

        font=(
            "Arial",
            40,
            "bold"
        ),

        fg="white",

        bg="black"

    )


    message.pack(
        expand=True
    )



    compteur = TIMEOUT



    def countdown():

        global screen_active


        nonlocal compteur



        uid = get_uid()



        # Badge remis

        if uid == AUTHORIZED_UID:

            print(
                "Badge retrouvé"
            )


            screen_active = False


            win.destroy()


            return



        # Compte à rebours

        if compteur > 0:


            message.config(

                text=
                f"Présentez votre badge NFC\n\n{compteur}"

            )


            compteur -= 1


            win.after(
                1000,
                countdown
            )


        else:


            print(
                "Badge absent -> verrouillage"
            )


            screen_active = False


            win.destroy()


            lock_windows()



    countdown()



# ==========================
# Surveillance
# ==========================

def monitor():

    global badge_lost


    uid = get_uid()



    if uid == AUTHORIZED_UID:

        badge_lost = False



    else:

        if not badge_lost:

            print(
                "Badge retiré"
            )


            badge_lost = True


            show_badge_screen()



    root.after(
        1000,
        monitor
    )



# ==========================
# Programme principal
# ==========================

root = tk.Tk()

root.withdraw()



print(
    "NFCGuard démarré"
)



start_tray()



root.after(
    1000,
    monitor
)



root.mainloop()