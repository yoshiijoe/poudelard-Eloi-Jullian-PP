def initialiser_personnage(nom, prenom, attributs):
    """
    Crée et retourne le dictionnaire du personnage.
    Argent départ : 100.
    Inventaire et Sortilèges : listes vides.
    """
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs  # C'est un dictionnaire (courage, etc.)
    }
    return joueur

def afficher_personnage(joueur):
    """
    Affiche toutes les infos du joueur (Nom, Argent, Inventaire, etc.).
    Astuce : Utiliser une boucle pour parcourir les attributs.
    """
    print(f"Profil de {joueur['Prenom']} {joueur['Nom']}")
    # Afficher le reste...
    pass

def modifier_argent(joueur, montant):
    """
    Ajoute (ou retire si négatif) le montant à l'argent du joueur.
    """
    # Code ici
    pass

def ajouter_objet(joueur, cle, objet):
    """
    Ajoute un objet à la liste spécifiée par 'cle' ("Inventaire" ou "Sortilèges").
    """
    # Vérifier si la clé existe, puis append() l'objet à la liste correspondante
    pass