from poudelard.utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from poudelard.univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet

def introduction():
    print("Bienvenue jeune sorcier🧙‍♂️dans le monde magique✨✨✨.")
    print("Ici tu vas devoir des choix qui auront tous une grande importance.")
    print("Alors choisi bien et bonne chance !")
    input("--- Appuyez sur ENTREE pour commencer votre aventure ---")

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
    print(f"Hagrid: Salut {personnage['Prenom']}!")
    print("Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.")
    print("")

    options = ["Oui", "Non"]

    choix = demander_choix("Voulez-vous suivre Hagrid ?", options)
    if choix == "Non":
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")

def acheter_fournitures(personnage):
    print("Bienvenue sur le Chemin de Traverse !")
    donnees_boutique = load_fichier("data/inventaire.json")
    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    boutique = []
    if type(donnees_boutique) == dict:
        for nom in donnees_boutique:
            prix = donnees_boutique[nom]
            boutique.append({"nom": nom, "prix": prix})
    else:
        boutique = donnees_boutique

    while len(objets_obligatoires) > 0:
        print("Catalogue des objets disponibles :")
        i = 0
        for objet in boutique:
            i = i + 1
            print(f"{i}. {objet['nom']} - {objet['prix']} galions")

        print(f"Vous avez {personnage['Argent']} galions.")
        chaine_objets = ", ".join(objets_obligatoires)
        print(f"Objets obligatoires restant à acheter : {chaine_objets}")

        choix = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, len(boutique))
        objet_choisi = boutique[choix - 1]

        if personnage['Argent'] < objet_choisi['prix']:
            print("Vous n'avez pas assez d'argent... Vous ne pouvez pas aller à Poudlard.")
            print("Fin de la partie.")
            exit()
        else:
            modifier_argent(personnage, -objet_choisi['prix'])
            ajouter_objet(personnage, "Inventaire", objet_choisi['nom'])
            print(f"Vous avez acheté : {objet_choisi['nom']} (-{objet_choisi['prix']} galions).")

            if objet_choisi['nom'] in objets_obligatoires:
                objets_obligatoires.remove(objet_choisi['nom'])

    print("Tous les objets obligatoires ont été achetés !")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {personnage['Argent']} galions.")
    print("Voici les animaux disponibles :")
    print("1. Chouette - 20 galions")
    print("2. Chat - 15 galions")
    print("3. Rat - 10 galions")
    print("4. Crapaud - 5 galions")

    choix_animal = demander_nombre("Quel animal voulez-vous ?", 1, 4)
    nom_animal = ""
    prix_animal = 0

    if choix_animal == 1:
        nom_animal = "Chouette"
        prix_animal = 20
    elif choix_animal == 2:
        nom_animal = "Chat"
        prix_animal = 15
    elif choix_animal == 3:
        nom_animal = "Rat"
        prix_animal = 10
    elif choix_animal == 4:
        nom_animal = "Crapaud"
        prix_animal = 5

    if personnage['Argent'] < prix_animal:
        print("Vous n'avez pas assez d'argent pour cet animal... C'est dommage.")
        print("Fin de la partie.")
        exit()

    modifier_argent(personnage, -prix_animal)
    ajouter_objet(personnage, "Inventaire", nom_animal)
    print(f"Vous avez choisi : {nom_animal} (-{prix_animal} galions).")

    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    afficher_personnage(personnage)
    return personnage

def lancer_chapitre_1():
    introduction()
    personnage = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(personnage)
    personnage = acheter_fournitures(personnage)
    print ("Fin du Chapitre 1 ! Votre aventure commence à Poudlard")
    return personnage