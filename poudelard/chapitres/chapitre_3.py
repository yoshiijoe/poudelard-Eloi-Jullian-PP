import json
import random
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


def apprendre_sorts(joueur):
    with open("data/sorts.json", "r", encoding="utf-8") as f:
        tous_les_sorts = json.load(f)

    offensifs = []
    defensifs = []
    utilitaires = []

    for sort in tous_les_sorts:
        if sort["type"] == "Offensif":
            offensifs.append(sort)
        elif sort["type"] == "Défensif":
            defensifs.append(sort)
        elif sort["type"] == "Utilitaire":
            utilitaires.append(sort)

    nouveaux_sorts = []

    index_off = random.randint(0, len(offensifs) - 1)
    nouveaux_sorts.append(offensifs[index_off])

    index_def = random.randint(0, len(defensifs) - 1)
    nouveaux_sorts.append(defensifs[index_def])

    while len(nouveaux_sorts) < 5:
        index_util = random.randint(0, len(utilitaires) - 1)
        sort_choisi = utilitaires[index_util]

        est_deja_pris = False
        for s in nouveaux_sorts:
            if s["nom"] == sort_choisi["nom"]:
                est_deja_pris = True

        if est_deja_pris == False:
            nouveaux_sorts.append(sort_choisi)

    print("      VOS PREMIERS COURS DE MAGIE")
    print("Après plusieurs cours et de travail acharné, ")
    print("vous avez appris 5 nouveaux sortilèges :\n")

    for sort in nouveaux_sorts:
        joueur["Sortilèges"].append(sort)
        print("  {} ({})".format(sort['nom'], sort['type']))

    input("Appuyez sur Entrée pour consulter le détail de vos sorts...")

    print("\nDESCRIPTION DE VOS NOUVEAUX POUVOIRS :")
    for sort in nouveaux_sorts:
        print("- {} : {}".format(sort['nom'], sort['description']))

    input("\nAppuyez sur Entrée pour passer au Quiz de Magie !")


def quiz_magie(joueur):
    with open("data/quiz_magie.json", "r", encoding="utf-8") as f:
        toutes_les_questions = json.load(f)

    questions_posees = []

    while len(questions_posees) < 4:
        index_hasard = random.randint(0, len(toutes_les_questions) - 1)
        question_hasard = toutes_les_questions[index_hasard]

        deja_posee = False
        for q in questions_posees:
            if q["question"] == question_hasard["question"]:
                deja_posee = True

        if deja_posee == False:
            questions_posees.append(question_hasard)

    score = 0
    print("          LE QUIZ DE MAGIE")
    print("Répondez aux 4 questions pour gagner des points.\n")

    for i in range(len(questions_posees)):
        q_data = questions_posees[i]
        print("QUESTION {}: {}".format(i + 1, q_data['question']))

        reponse_joueur = input("Votre réponse > ")

        if reponse_joueur == q_data["reponse"]:
            print(" Bonne réponse ! +25 points.")
            score = score + 25
        else:
            print(" Mauvaise réponse. C'était : {}".format(q_data['reponse']))
        print()

    return score


def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)

    points_gagnes = quiz_magie(personnage)

    maison_joueur = personnage["Maison"]
    actualiser_points_maison(maisons, maison_joueur, points_gagnes)

    print("\nScore final : {} points pour {} !".format(points_gagnes, maison_joueur))
    afficher_maison_gagnante(maisons)

    input(" Appuyez sur ENTREE pour voir votre profil mis à jour ")

    print("\nVoici votre profil mis à jour :")
    afficher_personnage(personnage)

    return personnage

