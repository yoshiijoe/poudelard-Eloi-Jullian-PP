import json


def demander_texte(message):
    texte = ""
    saisie_valide = False

    while saisie_valide == False:
        texte = input(message)
        if len(texte) > 0:
            saisie_valide = True
        else:
            print("Erreur : La saisie ne peut pas être vide.")

    return texte


def demander_nombre(message, min_val=None, max_val=None):
    nombre = 0
    saisie_valide = False

    while saisie_valide == False:
        saisie = input(message)

        if len(saisie) == 0:
            print("Erreur : La saisie ne peut pas être vide.")
        else:
            index_depart = 0
            if saisie[0] == '-':
                index_depart = 1

            est_numerique = True

            if index_depart == 1 and len(saisie) == 1:
                est_numerique = False

            for i in range(index_depart, len(saisie)):
                c = saisie[i]
                if c < '0':
                    est_numerique = False
                if c > '9':
                    est_numerique = False

            if est_numerique == False:
                print("Veuillez entrer uniquement des chiffres.")
            else:
                valeur = int(saisie)

                erreur_borne = False
                if min_val != None:
                    if valeur < min_val:
                        erreur_borne = True

                if max_val != None:
                    if valeur > max_val:
                        erreur_borne = True

                if erreur_borne == True:
                    print("Veuillez entrer un nombre entre {} et {}.".format(min_val, max_val))
                else:
                    nombre = valeur
                    saisie_valide = True

    return nombre


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print("{}. {}".format(i + 1, options[i]))

    choix_numero = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix_numero - 1]


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees