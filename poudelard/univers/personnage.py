from utils import *
def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs":
    }
    return joueur


def afficher_personnage(joueur):
    print(f" Profil de {joueur['Prenom']} {joueur['Nom']}")
    print(f"Argent : {joueur['Argent']} galions")
    print(f"Inventaire : {joueur['Inventaire']}")
    print(f"Attributs : {joueur['Attributs']}")


def modifier_argent(joueur, montant):
    montant += joueur["Argent"]
    return montant



def ajouter_objet(joueur, cle, objet):
    if cle in joueur and (cle == "Inventaire" or cle == "Sortilège"):
        joueur[cle].append(objet)
    else :
        print(f"Erreur : La catégorie '{cle}' n'existe pas ou n'est pas autorisée.")
    return joueur
