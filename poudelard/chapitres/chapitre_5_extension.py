import random
from poudelard.utils.input_utils import demander_choix
from poudelard.univers.personnage import afficher_personnage


def combat_basilic(joueur):
    pv_joueur = 100
    pv_basilic = 120
    combat_en_cours = True
    epee_disponible = False

    print("\nTom Jedusor invoque le Basilic il semble aussi long qu'une rame de métro !")
    print("Fumseck le Phénix survole la pièce et crève les yeux du serpent !")
    print("Le Basilic est aveuglé, mais il peut toujours vous entendre et vous mordre.")

    victoire = False

    while combat_en_cours == True:
        print("\nVos PV : {} | PV Basilic : {}".format(pv_joueur, pv_basilic))

        actions = ["Attaquer avec un sort", "Esquiver", "Chercher de l'aide"]
        if epee_disponible == True:
            actions.append("Utiliser l'Épée de Gryffondor")

        choix = demander_choix("Que voulez-vous faire ?", actions)

        tour_fini = False

        if choix == "Attaquer avec un sort":
            chance = random.randint(1, 10) + (joueur['Attributs']['intelligence'] // 2)
            if chance > 5:
                degats = random.randint(15, 25)
                pv_basilic = pv_basilic - degats
                print("Votre sort touche le monstre ! -{} PV.".format(degats))
            else:
                print("Le Basilic évite votre sort !")

        elif choix == "Esquiver":
            print("Vous vous préparez à éviter la prochaine attaque.")
            chance_esquive = random.randint(1, 10) + (joueur['Attributs']['courage'] // 2)
            if chance_esquive > 4:
                print("Esquive réussie ! Le Basilic mord le vide.")
                tour_fini = True

        elif choix == "Chercher de l'aide":
            if epee_disponible == False:
                print("Le Choixpeau Magique apparaît... Vous y trouvez l'Épée de Gryffondor !")
                epee_disponible = True
            else:
                print("Fumseck vous apporte une larme de Phénix et vous soigne !")
                pv_joueur = pv_joueur + 30

        elif choix == "Utiliser l'Épée de Gryffondor":
            chance_epee = random.randint(1, 10) + (joueur['Attributs']['courage'])
            if chance_epee > 6:
                degats = random.randint(40, 60)
                pv_basilic = pv_basilic - degats
                print("Vous enfoncez l'épée dans le palais du Basilic ! -{} PV.".format(degats))
            else:
                print("L'épée glisse sur les écailles du monstre !")

        if pv_basilic <= 0:
            print("\nLe Basilic s'effondre dans un dernier râle. Vous avez vaincu le monstre !")
            combat_en_cours = False
            victoire = True
        else:
            if tour_fini == False:
                degats_monstre = random.randint(15, 30)
                pv_joueur = pv_joueur - degats_monstre
                print("Le Basilic vous frappe avec sa queue ! -{} PV.".format(degats_monstre))

                if pv_joueur <= 0:
                    print("\nVous succombez aux blessures du Basilic... Fin du jeu.")
                    combat_en_cours = False
                    victoire = False

    return victoire


def conclusion_aventure(joueur, victoire):
    if victoire == True:
        print("\n" + "=" * 50)
        print("      FÉLICITATIONS JEUNE SORCIER")
        print("=" * 50)
        print("Grâce à votre courage et à l'honneur de {},".format(joueur['Maison']))
        print("vous, {} {}, avez sauvé Poudlard.".format(joueur['Prenom'], joueur['Nom']))
        print("Tom Jedusor disparaît dans un cri alors que vous détruisez son journal.")
        print("L'année se termine sous les acclamations de vos amis.")
        print("=" * 50)
    else:
        print("\nGAME OVER")


def lancer_chapitre_5(joueur, maisons):
    print("========================================")
    print("\n    CHAPITRE 5 : LA CHAMBRE DES SECRETS    ")
    print("\n========================================")
    print("Après avoir trouvé une série de personnes pétrifiées, dont Hermione,")
    print("vous avez enquêté et trouvé le responsable : un Basilic, un serpent géant qui se déplace dans les tuyaux.")
    print("Vous allez donc aux toilettes de Mimi Geignarde, car il s'y trouve une entrée.")
    print("Vous descendez par les tuyaux dans les profondeurs du château.")
    print("Tom Jedusor vous attend devant la statue de Salazar Serpentard.")

    a_gagne = combat_basilic(joueur)

    if a_gagne == True:
        conclusion_aventure(joueur, True)
    else:
        print("Poudlard est tombé aux mains des ténèbres...")

    return joueur