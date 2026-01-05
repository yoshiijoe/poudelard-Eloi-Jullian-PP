import json
import random
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    liste_joueurs_propre = []

    if type(equipe_data) == dict:
        for cle in equipe_data:
            liste_joueurs_propre.append(equipe_data[cle])
    else:
        for j in equipe_data:
            liste_joueurs_propre.append(j)

    if est_joueur == True and joueur is not None:
        equipe_finale = []

        nom_complet = "{} {} (Attrapeur)".format(joueur["Prenom"], joueur["Nom"])
        equipe_finale.append(nom_complet)

        for membre in liste_joueurs_propre:
            equipe_finale.append(membre)

        liste_joueurs_propre = equipe_finale

    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": liste_joueurs_propre
    }

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        buteur = ""
        if joueur_est_joueur == True:
            buteur = equipe_attaque["joueurs"][0]
        else:
            liste_joueurs = equipe_attaque["joueurs"]
            index_buteur = random.randint(0, len(liste_joueurs) - 1)
            buteur = liste_joueurs[index_buteur]

        equipe_attaque["score"] = equipe_attaque["score"] + 10
        equipe_attaque["a_marque"] = equipe_attaque["a_marque"] + 1

        print("{} marque un but pour {} ! (+10 points)".format(buteur, equipe_attaque["nom"]))

    else:
        equipe_defense["a_stoppe"] = equipe_defense["a_stoppe"] + 1
        print("{} bloque l'attaque !".format(equipe_defense["nom"]))


def apparition_vifdor():
    chance = random.randint(1, 6)
    if chance == 6:
        return True
    return False


def attraper_vifdor(e1, e2):
    equipe_gagnante = {}

    tirage = random.randint(1, 2)
    if tirage == 1:
        equipe_gagnante = e1
    else:
        equipe_gagnante = e2

    equipe_gagnante["score"] = equipe_gagnante["score"] + 150
    equipe_gagnante["attrape_vifdor"] = True

    return equipe_gagnante


def afficher_score(e1, e2):
    print("Score actuel :")
    print("{} : {} points".format(e1["nom"], e1["score"]))
    print("{} : {} points".format(e2["nom"], e2["score"]))


def afficher_equipe(maison, equipe):
    print("Équipe de {} :".format(maison))
    for membre in equipe["joueurs"]:
        print("- {}".format(membre))


def match_quidditch(joueur, maisons):
    with open("data/equipes_quidditch.json", "r", encoding="utf-8") as f:
        donnees_equipes = json.load(f)

    maison_joueur = joueur["Maison"]

    maisons_adverses = []
    for m in donnees_equipes:
        if m != maison_joueur:
            maisons_adverses.append(m)

    index_adv = random.randint(0, len(maisons_adverses) - 1)
    nom_adversaire = maisons_adverses[index_adv]

    data_joueur = donnees_equipes[maison_joueur]
    data_adversaire = donnees_equipes[nom_adversaire]

    equipe_joueur = creer_equipe(maison_joueur, data_joueur, True, joueur)
    equipe_adversaire = creer_equipe(nom_adversaire, data_adversaire, False)

    print()
    print("MATCH DE QUIDDITCH : {} VS {}".format(maison_joueur, nom_adversaire))
    print()

    afficher_equipe(maison_joueur, equipe_joueur)
    print()
    afficher_equipe(nom_adversaire, equipe_adversaire)
    print()

    print("Tu joues pour {} en tant qu'Attrapeur.".format(maison_joueur))
    print("Le match commence !")
    print()

    match_termine = False
    tour = 1

    while tour <= 20 and match_termine == False:
        print("--- Tour {} ---".format(tour))

        tentative_marque(equipe_joueur, equipe_adversaire, True)

        tentative_marque(equipe_adversaire, equipe_joueur, False)

        afficher_score(equipe_joueur, equipe_adversaire)

        est_present = apparition_vifdor()
        if est_present == True:
            print()
            print("LE VIF D'OR EST APPARU !")
            vainqueur_vif = attraper_vifdor(equipe_joueur, equipe_adversaire)
            print("Le Vif d'Or a été attrapé par {} ! (+150 points)".format(vainqueur_vif["nom"]))
            match_termine = True

        if match_termine == False:
            input("Appuyez sur Entrée pour le tour suivant...")
            print()
            tour = tour + 1

    print()
    print("--- FIN DU MATCH ---")
    afficher_score(equipe_joueur, equipe_adversaire)
    print()

    gagnant_match = ""
    if equipe_joueur["score"] > equipe_adversaire["score"]:
        gagnant_match = equipe_joueur["nom"]
    elif equipe_adversaire["score"] > equipe_joueur["score"]:
        gagnant_match = equipe_adversaire["nom"]
    else:
        gagnant_match = "Egalité"

    if gagnant_match == maison_joueur:
        print("VICTOIRE ! {} remporte le match !".format(maison_joueur))
        print("Ta maison gagne 500 points pour la Coupe.")
        actualiser_points_maison(maisons, maison_joueur, 500)
    elif gagnant_match == "Egalité":
        print("MATCH NUL ! Quelle intensité !")
        print("Les deux équipes reçoivent 200 points.")
        actualiser_points_maison(maisons, maison_joueur, 200)
        actualiser_points_maison(maisons, nom_adversaire, 200)
    else:
        print("DÉFAITE... {} remporte le match.".format(nom_adversaire))
        print("{} gagne 500 points pour la Coupe.".format(nom_adversaire))
        actualiser_points_maison(maisons, nom_adversaire, 500)


def lancer_chapitre4_quidditch(joueur, maisons):
    print("==================================================")
    print("      CHAPITRE 4 : LA GLOIRE DU QUIDDITCH")
    print("==================================================")
    print()

    match_quidditch(joueur, maisons)

    print()
    print("Fin du Chapitre 4 ! Quelle performance incroyable sur le terrain !")

    print()
    afficher_maison_gagnante(maisons)

    print()
    print("Voici ton profil final :")
    afficher_personnage(joueur)