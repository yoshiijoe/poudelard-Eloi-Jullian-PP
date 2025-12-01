from utils import *
def actualiser_points_maison(maisons, nom_maison, points) :
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    return maisons

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
    print(f"Gagnant(s) : {noms_propres} avec {score_max} points.")

    def repartition_maison(joueur, questions):
        attributs = {
            "courage": 0,
            "intelligence": 0,
            "loyauté": 0,
            "ambition": 0
        }
        questions = [
            (
                "Tu vois un ami en danger. Que fais-tu ?",
                [
                    "Je fonce l'aider",
                    "Je réfléchis à un plan",
                    "Je cherche de l’aide",
                    "Je reste calme et j’observe"
                ],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            ),
            (
                "Quel trait te décrit le mieux ?",
                [
                    "Courageux et loyal",
                    "Rusé et ambitieux",
                    "Patient et travailleur",
                    "Intelligent et curieux"
                ],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            ),
            (
                "Face à un défi difficile, tu...",
                [
                    "Fonces sans hésiter",
                    "Cherches la meilleure stratégie",
                    "Comptes sur tes amis",
                    "Analyses le problème"
                ],
                ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
            )
        ]




