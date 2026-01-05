import random
from poudelard.utils.input_utils import demander_choix
from poudelard.univers.personnage import afficher_personnage


def combat_basilic(joueur):
    pv_joueur = 100
    pv_basilic = 120
    combat_en_cours = True
    epee_disponible = False

    print("\nLe Basilic surgit des ombres ! Ses yeux sont jaunes et menaçants.")
    print("Fumseck le Phénix survole la pièce et crève les yeux du serpent !")
    print("Le Basilic est aveuglé, mais il peut toujours vous entendre et vous mordre.")

    while combat_en_cours:
        print(f"\nVos PV : {pv_joueur} | PV Basilic : {pv_basilic}")

        actions = ["Attaquer avec un sort", "Esquiver", "Chercher de l'aide"]
        if epee_disponible:
            actions.append("Utiliser l'Épée de Gryffondor")

        choix = demander_choix("Que voulez-vous faire ?", actions)

        if choix == "Attaquer avec un sort":
            chance = random.randint(1, 10) + (joueur['Attributs']['intelligence'] // 2)
            if chance > 5:
                degats = random.randint(15, 25)
                pv_basilic -= degats
                print(f"Votre sort touche le monstre ! -{degats} PV.")