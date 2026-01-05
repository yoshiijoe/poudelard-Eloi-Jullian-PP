from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch
from poudelard.chapitres.chapitre_5_extension import lancer_chapitre_5


def afficher_menu_principal():
    print("========================================")
    print("      BIENVENUE A POUDLARD")
    print("========================================")
    print("1. Lancer l'aventure (Chapitres 1 à 4)")
    print("2. Quitter le jeu")
    print("========================================")


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    continuer = True

    while continuer:
        afficher_menu_principal()
        choix = input("Votre choix : ")

        if choix == "1":
            joueur = lancer_chapitre_1()

            lancer_chapitre_2(joueur)

            lancer_chapitre_3(joueur, maisons)

            lancer_chapitre4_quidditch(joueur, maisons)

            lancer_chapitre_5(joueur, maisons)

            print()
            print("Félicitations ! Vous avez terminé l'aventure.")
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "2":
            print("Au revoir et à bientôt à Poudlard !")
            continuer = False

        else:
            print("Choix invalide. Veuillez taper 1 ou 2.")
            print()
