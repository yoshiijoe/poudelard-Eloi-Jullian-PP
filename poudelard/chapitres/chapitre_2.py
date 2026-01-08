from poudelard.utils.input_utils import demander_choix
from poudelard.univers.personnage import afficher_personnage

def rencontrer_amis(joueur):
    print("\n Dans le Poudlard Express ")
    print("Un garçon roux entre dans votre compartiment, l'air amical.")

    option_ron = ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    choix_ron = demander_choix("Salut ! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?", option_ron)

    if choix_ron == option_ron[0]:
        print("Ron sourit : Génial ! Tu verras, Poudlard, c'est incroyable !")
        joueur['Attributs']['loyauté'] = joueur['Attributs']['loyauté'] + 1
    else:
        print("Ron hausse les épaules et va chercher une autre place.")
        joueur['Attributs']['ambition'] = joueur['Attributs']['ambition'] + 1

    print("\nUne fille entre ensuite, portant déjà une pile de livres.")
    option_hermione = ["Oui, j'adore apprendre !", "Euh... non, je préfère l'aventure."]
    choix_hermione = demander_choix("Je suis Hermione Granger. Vous avez lu 'Histoire de la Magie' ?", option_hermione)

    if choix_hermione == option_hermione[0]:
        print("Hermione sourit : C'est fascinant, n'est-ce pas ?")
        joueur['Attributs']['intelligence'] = joueur['Attributs']['intelligence'] + 1
    else:
        print("Hermione fronce les sourcils : Il faudrait pourtant s'y mettre !")
        joueur['Attributs']['courage'] = joueur['Attributs']['courage'] + 1

    print("\nPuis un garçon blond entre avec un air arrogant.")
    option_drago = ["Je lui serre la main.", "Je l'ignore.", "Je lui réponds avec arrogance."]
    choix_drago = demander_choix("Je suis Drago Malefoy. Mieux vaut bien choisir ses amis, non ?", option_drago)

    if choix_drago == option_drago[0]:
        print("Drago vous regarde avec un air satisfait.")
        joueur['Attributs']['ambition'] = joueur['Attributs']['ambition'] + 1
    elif choix_drago == option_drago[1]:
        print("Drago fronce les sourcils, vexé : Tu le regretteras !")
        joueur['Attributs']['loyauté'] = joueur['Attributs']['loyauté'] + 1
    else:
        print("Drago semble furieux de votre audace.")
        joueur['Attributs']['courage'] = joueur['Attributs']['courage'] + 1


def ceremonie_repartition(joueur):
    print("   LA CÉRÉMONIE DE RÉPARTITION   ")
    print("Le Choixpeau Magique est posé sur votre tête...\n")

    scores = joueur['Attributs']

    maison_gagnante = ""
    max_valeur = -1

    for nom_attribut in scores:
        valeur = scores[nom_attribut]
        if valeur > max_valeur:
            max_valeur = valeur
            maison_gagnante = nom_attribut

    maison = ""
    if maison_gagnante == "courage":
        maison = "Gryffondor"
    elif maison_gagnante == "intelligence":
        maison = "Serdaigle"
    elif maison_gagnante == "loyauté":
        maison = "Poufsouffle"
    else:
        maison = "Serpentard"

    print("CHOIXPEAU : 'Difficile... très difficile... Mais je sais !'")
    print("CHOIXPEAU : 'Ce sera... {} !'".format(maison))

    joueur["Maison"] = maison
    return maison


def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    input(" Appuyez sur ENTREE pour passer à la suite ")
    ceremonie_repartition(joueur)
    input(" Appuyez sur ENTREE pour voir votre profil mise à jour ")
    print("\nVoici votre profil mis à jour :")
    afficher_personnage(joueur)
    print("Maison : {}".format(joueur['Maison']))
    return joueur