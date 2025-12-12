from poudelard.utils.input_utils import demander_texte, demander_nombre, demander_choix
from poudelard.univers.personnage import initialiser_personnage, afficher_personnage

def introduction():
    print("Bienvenue jeune sorcier🧙‍♂️dans le monde magique✨✨✨.")
    print("Ici tu vas devoir des choix qui auront tous une grande importance.")
    print("Alors choisi bien et bonne chance !")
    input()

def creer_personnage():
    nom = demander_texte("Choisi ton nom jeune sorcier : ")
    prenom = demander_texte("Choisi ton prénom jeune sorcier : ")

    print("Définissez vos attributs (entre 1 et 10) :")
    courage = demander_nombre("À quel point veux-tu être courageux (1 à 10) : ", 1, 10)
    intelligence = demander_nombre("À quel point veux-tu être intelligent (1 à 10) : ", 1, 10)
    loyaute = demander_nombre("À quel point veux-tu être loyal (1 à 10) : ", 1, 10)
    ambition = demander_nombre("À quel point veux-tu être ambitieux (1 à 10) : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyaute": loyaute,
        "ambition": ambition
    }

    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)

    return joueur


def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée")
    print("du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à")
    print("l’école de sorcellerie de Poudlard ! »")

    options = ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]

    choix = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", options)

    if choix == "Non, je préfère rester avec l’oncle Vernon...":
        print("Vous déchirez la lettre:")
        print("Le magicien Marius apparaît pour la première fois.")
        print("Il vous jette un sort, vous ne pourrez plus jamais aller en cours à Poudlard.")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()

def rencontrer_hagrid(personnage):
    print("Hagrid: Salut Harry !")
    print("Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.")
    print("")

    options = ["1. Oui", "2. Non"]

    choix = demander_choix("Voulez-vous suivre Hagrid ?", options)
    if choix ==


