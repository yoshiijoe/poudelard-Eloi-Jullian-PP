def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return joueur


def afficher_personnage(joueur):
    print("Profil de {} {}".format(joueur['Prenom'], joueur['Nom']))
    print("Argent : {} galions".format(joueur['Argent']))

    inv_str = ", ".join(joueur['Inventaire'])
    print("Inventaire : {}".format(inv_str))

    print("Sortilèges :")
    for sort in joueur['Sortilèges']:
        if type(sort) == dict:
            print("- {}".format(sort['nom']))
        else:
            print("- {}".format(sort))

    print("Attributs :")
    for cle, valeur in joueur['Attributs'].items():
        print("   {}: {}".format(cle, valeur))


def modifier_argent(joueur, montant):
    joueur["Argent"] += montant


def ajouter_objet(joueur, cle, objet):
    if cle == "Inventaire" or cle == "Sortilèges":
        joueur[cle].append(objet)
    else:
        print("Erreur : La catégorie '{}' n'existe pas ou n'est pas autorisée.".format(cle))
