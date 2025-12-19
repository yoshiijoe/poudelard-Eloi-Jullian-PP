import random
from poudelard.utils.input_utils import load_fichier, demander_texte
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


def apprendre_sorts(joueur):
    tous_les_sorts = load_fichier("data/sorts.json")

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

    while len(nouveaux_sorts) < 5:
        sort_choisi = random.choice(utilitaires)
        est_deja_pris = False
        for s in nouveaux_sorts:
            if s["nom"] == sort_choisi["nom"]:
                est_deja_pris = True

        if est_deja_pris == False:
            nouveaux_sorts.append(sort_choisi)

    print("Tu commences tes cours de magie à Poudlard...")
    print()

    for sort in nouveaux_sorts:
        joueur["Sortilèges"].append(sort)
        print(f"Tu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("\nTu as terminé ton apprentissage de base !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for sort in nouveaux_sorts:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")


def quiz_magie(joueur):
    toutes_les_questions = load_fichier("data/quiz_magie.json")
    questions_posees = []

    while len(questions_posees) < 4:
        question_hasard = random.choice(toutes_les_questions)
        if question_hasard not in questions_posees:
            questions_posees.append(question_hasard)

    score = 0
    print("\nBienvenue au quiz de magie de Poudlard !")
    print("Réponds aux 4 questions pour gagner des points pour ta maison.\n")

    for i in range(len(questions_posees)):
        q_data = questions_posees[i]
        print(f"{i + 1}. {q_data['question']}")

        reponse_joueur = demander_texte("> ")

        if reponse_joueur.lower() == q_data["reponse"].lower():
            print("Bonne réponse ! +25 points.")
            score = score + 25
        else:
            print(f"Mauvaise réponse. C'était : {q_data['reponse']}")
        print()

    return score


def lancer_chapitre_3(personnage, maisons):
    print("\n--- Chapitre 3 : Les cours et la découverte de Poudlard ---")

    apprendre_sorts(personnage)

    points_gagnes = quiz_magie(personnage)

    maison_joueur = personnage["Maison"]
    actualiser_points_maison(maisons, maison_joueur, points_gagnes)

    print(f"\nScore final du quiz : {points_gagnes} points pour {maison_joueur} !")
    afficher_maison_gagnante(maisons)

    print("\nÉtat de votre personnage après les cours :")
    afficher_personnage(personnage)

    return personnage