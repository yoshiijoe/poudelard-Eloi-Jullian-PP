import random
from poudelard.utils.input_utils import demander_choix
from poudelard.univers.personnage import afficher_personnage


def combat_basilic(joueur):
    pv_joueur = 100
    pv_basilic = 120
    combat_en_cours = True
    epee_disponible = False

    print("\nTom Jedusor invoque le Basilic il semble aussi long qu'une ramede métro !")
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
            else:
                print("Le Basilic évite votre sort !")

        elif choix == "Esquiver":
            print("Vous vous préparez à éviter la prochaine attaque.")
            chance_esquive = random.randint(1, 10) + (joueur['Attributs']['courage'] // 2)
            if chance_esquive > 4:
                print("Esquive réussie ! Le Basilic mord le vide.")
                continue

        elif choix == "Chercher de l'aide":
            if not epee_disponible:
                print("Le Choixpeau Magique apparaît... Vous y trouvez l'Épée de Gryffondor !")
                epee_disponible = True
            else:
                print("Fumseck vous apporte une larme de Phénix et vous soigne !")
                pv_joueur += 30

        elif choix == "Utiliser l'Épée de Gryffondor":
            chance_epee = random.randint(1, 10) + (joueur['Attributs']['courage'])
            if chance_epee > 6:
                degats = random.randint(40, 60)
                pv_basilic -= degats
                print(f"COUP CRITIQUE ! Vous enfoncez l'épée dans le palais du Basilic ! -{degats} PV.")
            else:
                print("L'épée glisse sur les écailles du monstre !")

        if pv_basilic <= 0:
            print("\nLe Basilic s'effondre dans un dernier râle. Vous avez vaincu le monstre !")
            combat_en_cours = False
        else:
            degats_monstre = random.randint(15, 30)
            pv_joueur -= degats_monstre
            print(f"Le Basilic vous frappe avec sa queue ! -{degats_monstre} PV.")

            if pv_joueur <= 0:
                print("\nVous succombez aux blessures du Basilic... Fin du jeu.")
                exit()

    return True


def conclusion_aventure(joueur, victoire):
    if victoire:
        print("\n" + "=" * 50)
        print("      FÉLICITATIONS JEUNE SORCIER")
        print("=" * 50)
        print(f"Grâce à votre {joueur['Maison']}, vous avez sauvé Poudlard.")
        print("Tom Jedusor disparaît dans un cri alors que vous détruisez son journal.")
        print("L'année se termine sous les acclamations de vos amis.")
        print("=" * 50)

def lancer_chapitre_5(joueur, maisons):
    print("========================================")
    print("\n    CHAPITRE 5 : LA CHAMBRE DES SECRETS    ")
    print("\n========================================")
    print("Après avoir trouvé une série de personnes pétrifiées, dont Hermione,")
    print("vous avez enquêté et trouvé le responsable : un Basilic, un serpent géant qui se déplace dans les tuyaux.")
    print("Vous allez donc aux toilettes de Mimi Geignarde, car il s'y trouve une entrée.")
    print("Vous descendez par les tuyaux dans les profondeurs du château.")
    print("Tom Jedusor vous attend devant la statue de Salazar Serpentard.")

    victoire = combat_basilic(joueur)
    conclusion_aventure(joueur, victoire)

    return joueur