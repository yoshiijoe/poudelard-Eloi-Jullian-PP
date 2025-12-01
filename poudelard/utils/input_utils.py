import json

def demander_texte(message):
    texte = input(message).strip()
    while len(texte) == 0:
        print("Erreur : La saisie ne peut pas être vide.")
        texte = input(message).strip()
    return texte


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()
        if len(saisie) == 0:
            print("Erreur : La saisie ne peut pas être vide.")
            continue
        est_negatif = False
        chiffres = saisie
        if saisie[0] == '-':
            est_negatif = True
            chiffres = saisie[1:]
        if len(chiffres) == 0:
            print("Veuillez entrer un nombre valide.")
            continue
        est_valide = True
        for c in chiffres:
            if c < '0' or c > '9':
                est_valide = False
                break
        if not est_valide:
            print("Veuillez entrer uniquement des chiffres.")
            continue
        nombre = 0
        for c in chiffres:
            nombre = nombre * 10 + (ord(c) - ord('0'))
        if est_negatif:
            nombre = -nombre
        if min_val is not None and nombre < min_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue
        if max_val is not None and nombre > max_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            continue
        return nombre

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    choix_numero = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix_numero - 1]

def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees
