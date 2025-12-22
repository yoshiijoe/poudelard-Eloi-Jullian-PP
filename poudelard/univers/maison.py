from poudelard.utils.input_utils import demander_nombre

maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        print("La maison {} a reçu (ou perdu) des points.".format(nom_maison))
        print("Nouveau score de {} : {} points.".format(nom_maison, maisons[nom_maison]))


def afficher_maison_gagnante(maisons):
    score_max = maisons["Gryffondor"]
    gagnants = ["Gryffondor"]

    if maisons["Serpentard"] > score_max:
        score_max = maisons["Serpentard"]
        gagnants = ["Serpentard"]
    elif maisons["Serpentard"] == score_max:
        gagnants.append("Serpentard")

    if maisons["Poufsouffle"] > score_max:
        score_max = maisons["Poufsouffle"]
        gagnants = ["Poufsouffle"]
    elif maisons["Poufsouffle"] == score_max:
        gagnants.append("Poufsouffle")

    if maisons["Serdaigle"] > score_max:
        score_max = maisons["Serdaigle"]
        gagnants = ["Serdaigle"]
    elif maisons["Serdaigle"] == score_max:
        gagnants.append("Serdaigle")

    noms_propres = ", ".join(gagnants)
    print("Gagnant(s) : {} avec {} points.".format(noms_propres, score_max))

def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur["Attributs"]

    scores["Gryffondor"] += attributs["courage"] * 2
    scores["Serpentard"] += attributs["ambition"] * 2
    scores["Poufsouffle"] += attributs["loyauté"] * 2
    scores["Serdaigle"] += attributs["intelligence"] * 2

    for question_tuple in questions:
        texte_question = question_tuple[0]
        choix_possibles = question_tuple[1]
        maisons_associees = question_tuple[2]

        print(texte_question)

        for i in range(len(choix_possibles)):
            print("{}. {}".format(i + 1, choix_possibles[i]))

        reponse = demander_nombre("Ton choix : ", 1, len(choix_possibles))

        index_choisi = reponse - 1
        maison_gagnante_question = maisons_associees[index_choisi]

        scores[maison_gagnante_question] += 3
        print()

    print("Résumé des scores :")
    for maison, points in scores.items():
        print("{} : {} points".format(maison, points))
    print()

    meilleure_maison = ""
    score_max = -1

    for maison, points in scores.items():
        if points > score_max:
            score_max = points
            meilleure_maison = maison

    return meilleure_maison
        






