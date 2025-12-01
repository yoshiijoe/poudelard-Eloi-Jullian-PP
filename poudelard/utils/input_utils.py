import json
import os

def demander_texte(message):
    nom = input("Entrez le nom de votre apprenti magicien🧙:")
    while len(nom) < 1:
        nom = input("Nom invalide. Entrez le nom de votre apprenti :")
















    """
    Demande une saisie utilisateur et s'assure qu'elle n'est pas vide.
    Utilise .strip() pour nettoyer les espaces.
    """
    # TANT QUE la saisie est vide :
    #    Redemander
    # RETOURNER la saisie nettoyée
    pass  # À remplacer par ton code

def demander_nombre(message, min_val=None, max_val=None):
    """
    Demande un entier. Vérifie que c'est un nombre valide et qu'il est
    compris entre min_val et max_val (si spécifiés).
    """
    # Boucle infinie pour demander :
    #    1. Récupérer la saisie (input)
    #    2. Vérifier si c'est un nombre entier (Attention : le sujet suggère de vérifier les chiffres manuellement ou via conversion)
    #    3. Si c'est un nombre, vérifier s'il est entre min_val et max_val
    #    4. Si tout est bon -> RETURN nombre
    #    5. Sinon -> Afficher message d'erreur et recommencer
    pass

def demander_choix(message, options):
    """
    Affiche une liste numérotée d'options et demande à l'utilisateur de choisir un numéro.
    Utilise demander_nombre() pour récupérer le choix.
    """
    # 1. Afficher le message
    # 2. Pour chaque option dans la liste 'options' :
    #      Afficher "i. Option" (ex: 1. Oui)
    # 3. Appeler demander_nombre() avec min=1 et max=len(options)
    # 4. Retourner l'élément correspondant dans la liste (Attention aux index : choix 1 = index 0)
    pass

def load_fichier(chemin_fichier):
    """
    Charge un fichier JSON et retourne son contenu.
    Utilise l'encodage utf-8.
    """
    # Ouvrir le fichier avec open() en mode lecture 'r' et encoding='utf-8'
    # Utiliser json.load(f)
    # Retourner les données
    pass