#Apprentissage des sorts et quiz magique page 29
import json
import random
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
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

    nouveaux_sorts.append(random.choice(offensifs))
    nouveaux_sorts.append(random.choice(defensifs))

    compteur_utilitaire = 0
    while compteur_utilitaire < 3:
        sort_choisi = random.choice(utilitaires)

        est_deja_pris = False
        for s in nouveaux_sorts:
            if s["nom"] == sort_choisi["nom"]:
                est_deja_pris = True

        if est_deja_pris == False:
            nouveaux_sorts.append(sort_choisi)
            compteur_utilitaire += 1

    print("Tu commences tes cours de magie à Poudlard...")
    print()

    for sort in nouveaux_sorts:
        joueur["Sortilèges"].append(sort)

        print("Tu viens d'apprendre le sortilège : {} ({})".format(sort["nom"], sort["type"]))

        input("Appuie sur Entrée pour continuer...")

    print()
    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")

    for sort in nouveaux_sorts:
        print("- {} ({}) : {}".format(sort["nom"], sort["type"], sort["description"]))


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        toutes_les_questions = json.load(f)

    questions_posees = []

    while len(questions_posees) < 4:
        question_hasard = random.choice(toutes_les_questions)
        if question_hasard not in questions_posees:
            questions_posees.append(question_hasard)

    score = 0

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")
    print()

    for i in range(len(questions_posees)):
        q_data = questions_posees[i]
        print("{}. {}".format(i + 1, q_data["question"]))

        reponse_joueur = input("> ")

        if reponse_joueur.strip().lower() == q_data["reponse"].strip().lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score += 25
        else:
            print("Mauvaise réponse. La bonne réponse était {}.".format(q_data["reponse"]))
        print()

    print("Score obtenu : {} points".format(score))
    return score


def lancer_chapitre_3(personnage, maisons):
    print(" Chapitre 3 : Les cours et la découverte de Poudlard ")
    print()

    apprendre_sorts(personnage)

    points_gagnes = quiz_magie(personnage)

    maison_joueur = personnage["Maison"]

    actualiser_points_maison(maisons, maison_joueur, points_gagnes)

    afficher_maison_gagnante(maisons)

    print()
    afficher_personnage(personnage)