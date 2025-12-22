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

    print("\n" + "-" * 50)
    print("      VOS PREMIERS COURS DE MAGIE")
    print("-" * 50)
    print("Après plusieurs cours et de travaille acharnée, ")
    print("vous avez appris 5 nouveaux sortilèges :\n")

    for sort in nouveaux_sorts:
        joueur["Sortilèges"].append(sort)
        print(f"  {sort['nom']} ({sort['type']})")

    print("\n" + "-" * 50)
    input("Appuyez sur Entrée pour consulter le détail de vos sorts...")

    print("\nDESCRIPTION DE VOS NOUVEAUX POUVOIRS :")
    for sort in nouveaux_sorts:
        print(f"- {sort['nom']} : {sort['description']}")

    print("-" * 50)
    input("\nAppuyez sur Entrée pour passer au Quiz de Magie !")


def quiz_magie(joueur):
    toutes_les_questions = load_fichier("data/quiz_magie.json")
    questions_posees = []

    while len(questions_posees) < 4:
        question_hasard = random.choice(toutes_les_questions)
        if question_hasard not in questions_posees:
            questions_posees.append(question_hasard)

    score = 0
    print("\n" + "-" * 50)
    print("          LE QUIZ DE MAGIE")
    print("-" * 50)
    print("Répondez aux 4 questions pour gagner des points.\n")

    for i in range(len(questions_posees)):
        q_data = questions_posees[i]
        print(f"QUESTION {i + 1}: {q_data['question']}")

        reponse_joueur = demander_texte("Votre réponse > ")

        if reponse_joueur.lower() == q_data["reponse"].lower():
            print(" Bonne réponse ! +25 points.")
            score = score + 25
        else:
            print(f" Mauvaise réponse. C'était : {q_data['reponse']}")
        print()

    return score


def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)

    points_gagnes = quiz_magie(personnage)

    maison_joueur = personnage["Maison"]
    actualiser_points_maison(maisons, maison_joueur, points_gagnes)

    print(f"\nScore final : {points_gagnes} points pour {maison_joueur} !")
    afficher_maison_gagnante(maisons)

    input("--- Appuyez sur ENTREE pour voir votre profil mise à jour ---" )

    print("\nVoici votre profil mis à jour :")
    afficher_personnage(personnage)

    return personnage

