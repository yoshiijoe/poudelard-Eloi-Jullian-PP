from utils.input_utils import demander_choix


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("Un garçon roux entre dans votre compartiment, l'air amical.")

    choix_ron = demander_choix("Salut ! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?",
                               ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])

    if choix_ron == 1:
        print("Ron sourit : Génial ! Tu verras, Poudlard, c'est incroyable !")
        joueur['Attributs']['loyauté'] += 1
    else:
        print("Ron hausse les épaules et va chercher une autre place.")
        joueur['Attributs']['ambition'] += 1

    print("Une fille entre ensuite, portant déjà une pile de livres.")

    choix_hermione = demander_choix(
        "Bonjour, je m'appelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie' ?",
        ["Oui, j'adore apprendre de nouvelles choses !", "Euh... non, je préfère les aventures aux bouquins."])

    if choix_hermione == 1:
        print("Hermione sourit : C'est fascinant, n'est-ce pas ?")
        joueur['Attributs']['intelligence'] += 1
    else:
        print("Hermione fronce les sourcils : Il faudrait pourtant s'y mettre un jour !")
        joueur['Attributs']['courage'] += 1

    print("Puis un garçon blond entre avec un air arrogant.")

    choix_drago = demander_choix(
        "Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?",
        ["Je lui serre la main poliment.", "Je l'ignore complètement.", "Je lui réponds avec arrogance."])

    if choix_drago == 1:
        print("Drago vous regarde avec un air satisfait.")
        joueur['Attributs']['ambition'] += 1
    elif choix_drago == 2:
        print("Drago fronce les sourcils, vexé : Tu le regretteras !")
        joueur['Attributs']['loyauté'] += 1
    else:
        print("Drago semble furieux de votre audace.")
        joueur['Attributs']['courage'] += 1

    print("Le train continue sa route. Le château de Poudlard se profile à l'horizon...")
    print(
        f"Tes choix semblent déjà en dire long sur ta personnalité !\nTes attributs mis à jour : {joueur['Attributs']}")