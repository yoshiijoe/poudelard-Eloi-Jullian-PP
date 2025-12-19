from poudelard.chapitres.chapitre_1 import lancer_chapitre_1
from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from poudelard.chapitres.chapitre_3 import lancer_chapitre_3
from poudelard.utils.input_utils import demander_nombre


def afficher_menu_principal():
    print("\n" + "=" * 30)
    print("       MENU PRINCIPAL")
    print("=" * 30)
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")
    print("=" * 30)


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serdaigle": 0,
        "Poufsouffle": 0,
        "Serpentard": 0
    }

    while True:
        afficher_menu_principal()
        choix = demander_nombre("Votre choix : ", 1, 2)

        if choix == 1:
            personnage = lancer_chapitre_1()
            personnage = lancer_chapitre_2(personnage)
            personnage = lancer_chapitre_3(personnage, maisons)
            print("\nFin de l'aventure disponible pour le moment !")
        elif choix == 2:
            print("Merci d'avoir joué ! À bientôt jeune sorcier.")
            break
        else:
            print("Choix invalide, veuillez recommencer.")