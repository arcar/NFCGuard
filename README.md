# NFCGuard

## Verrouillage Windows par badge NFC

NFCGuard est une application Python permettant de sécuriser une session Windows avec un badge NFC.

Le fonctionnement est simple :

1. Un badge NFC autorisé est posé sur un lecteur USB.
2. NFCGuard surveille en permanence la présence du badge.
3. Lorsque le badge est retiré :
   - un écran plein écran apparaît ;
   - le logo personnalisé est affiché ;
   - un compte à rebours démarre ;
   - si le badge n'est pas reposé avant la fin du délai, Windows verrouille automatiquement la session.
4. Après reconnexion Windows, NFCGuard reprend automatiquement son fonctionnement.

---

# Fonctionnalités

## Gestion NFC

- Lecture de l'UID unique d'un badge NFC.
- Surveillance permanente du badge.
- Support des lecteurs NFC USB compatibles PC/SC.
- Reconnexion automatique du lecteur.
- Gestion des badges absents.

## Sécurité Windows

- Verrouillage automatique de session avec l'API Windows :


LockWorkStation()


- Fonctionne avec le verrouillage natif Windows.
- Compatible avec Windows 10 et Windows 11.

## Interface utilisateur

- Fonctionnement silencieux avec `pythonw.exe`.
- Icône dans la zone de notification Windows.
- Affichage plein écran personnalisé.
- Logo personnalisable.
- Compte à rebours avant verrouillage.
- Protection contre la fermeture accidentelle de la fenêtre.

---

# Architecture du projet

````
NFCGuard
│
├── main.py # Programme principal
├── nfc_reader.py # Communication avec le lecteur NFC
├── tray.py # Gestion de l'icône Windows
├── config.py # Paramètres NFCGuard
│
├── logo.png # Image affichée lors du retrait badge
├── icon.ico # Icône de notification
│
├── requirements.txt # Dépendances Python
├── startup.bat # Script de démarrage
│
└── README.md # Documentation

````
---

# Configuration nécessaire

## Système

Compatible :

- Windows 10
- Windows 11

Matériel :

- Lecteur NFC USB compatible PC/SC

Exemples :

- ACS ACR122U
- Lecteurs CCID compatibles Windows

---

# Python

## Version utilisée :


Python 3.12


## Vérification :

```powershell
py -3.12 --version
````

Même si Python 3.14 est installé sur la machine, NFCGuard doit être lancé avec Python 3.12.

---
# Installation
## Installer les dépendances

Dans le dossier NFCGuard :
````
py -3.12 -m pip install -r requirements.txt
````
Ou manuellement :
````
py -3.12 -m pip install pyscard pillow pystray
````
## Fichier requirements.txt

Créer : requirements.txt

avec :
````
pyscard
pillow
pystray
````
----

# Configuration NFC

Modifier : config.py

Exemple :
````
AUTHORIZED_UID = "47:98:A7:6F"

TIMEOUT = 3

LOGO = "logo.png"
````
AUTHORIZED_UID correspond à l'identifiant unique du badge.

Exemple :
````
47:98:A7:6F
````
## Pour récupérer l'UID :

Lancer :
````
py -3.12 main.py
````
Présenter le badge.

La console affiche :

UID détecté : 47:98:A7:6F

Copier cette valeur dans config.py.

## TIMEOUT

Définit le temps avant verrouillage.

Exemple : TIMEOUT = 3

Résultat :

Badge retiré

3

2

1

Verrouillage Windows 

## LOGO

Chemin du logo affiché.

Exemple : LOGO = "logo.png"

Le fichier doit être dans le dossier NFCGuard.

---

# Premier lancement

Avant le démarrage automatique, tester manuellement :
````
py -3.12 main.py
````
Vérifier :

l'icône NFCGuard apparaît ;     
le badge est détecté ;  
le retrait du badge affiche l'écran ;   
le verrouillage fonctionne.     
Démarrage automatique Windows

## NFCGuard doit être lancé automatiquement à chaque ouverture de session.

### Utiliser : Planificateur de tâches Windows      

### Création de la tâche
````
Nom : NFCGuard  
````
### Déclencheur
````
Choisir : À l'ouverture de session
Action
````
### Programme :
````
Exemple : C:\Users\Utilisateur\AppData\Local\Programs\Python\Python312\pythonw.exe
````
### Arguments :
````
"C:\NFCGuard\main.py"
````
### Démarrer dans :
````
C:\NFCGuard
````
---

# Important

Utiliser :
````
pythonw.exe et non : python.exe
````
Différence :


python.exe	ouvre une console               
pythonw.exe	fonctionnement silencieux       

---


## Utilisation

Fonctionnement normal :

Badge NFC présent

        ↓

Session Windows active

        ↓

Surveillance permanente
Badge retiré

Après retrait :

Badge retiré

````
+--------------------------+
|                          |
|          LOGO            |
|                          |
|   Présentez le badge     |
|                          |
|            3             |
|                          |
+--------------------------+
````

        ↓

Badge remis :
Retour normal


OU


Temps écoulé :

Verrouillage Windows
Après verrouillage Windows

Lorsque l'utilisateur se reconnecte :

Ouverture session

        ↓

NFCGuard continue

        ↓

Nouvelle lecture du badge

Le lecteur NFC est automatiquement réutilisé.

---
# Dépannage
Le module smartcard manque

Erreur : ModuleNotFoundError: No module named 'smartcard'

Solution :
````
py -3.12 -m pip install pyscard
````
Le module PIL manque

Erreur :`ModuleNotFoundError: No module named 'PIL'

Solution :
````
py -3.12 -m pip install pillow
````
Le lecteur NFC n'est pas détecté

Vérifier :

lecteur branché ;       
pilotes installés ;     
service Windows Smart Card actif.

Tester :
````
py -3.12 main.py
````
Présenter le badge.

Résultat attendu :
````
UID détecté : XX:XX:XX:XX
````
L'icône n'apparaît pas

Vérifier :

utilisation de pythonw.exe ;    
tâche Windows configurée avec utilisateur connecté ;    
autorisation des icônes dans la barre système.

---
# Sécurité

NFCGuard ne stocke aucune donnée personnelle.

Les seules informations utilisées sont :

UID du badge NFC ;      
configuration locale ;  
état de présence du badge.

Aucune donnée n'est envoyée sur Internet.


---
# Améliorations possibles

## Évolutions futures :

Plusieurs badges autorisés.     
Liste blanche de badges.        
Historique des événements.      
Journal de présence.    
Interface graphique de configuration.   
Installation automatique.       
Service Windows professionnel.  
Signature numérique de l'application.   
Licence

Projet personnel.

NFCGuard
Python 3.12
Windows 10 / Windows 11