# Poudelard

#### Description :
jeu de rôle textuel développé en Python où le joueur incarne un jeune sorcier.
Le jeu suit une progression en 5 chapitres : de l'achat des fournitures 
sur le Chemin de Traverse jusqu'au combat final dans la Chambre des Secrets.

#### Contributeurs:
Adrien JULLIAN - Philéas ELOI

Installation

    Cloner le dépôt :
git clone https://github.com/votre-utilisateur/poudelard.git

#### Utilisation:
Pour lancer le jeu, exécutez le fichier main.py

#### Fonctionnalités Principales:

   - Création de personnage : Système d'attributs personnalisables (courage, intelligence, loyauté, ambition).
   - Gestion d'inventaire : Achat dynamique via des fichiers de données JSON.
   - Cérémonie de Répartition : Algorithme déterminant la maison en fonction des choix passés.
   - Système de Combat : Duel au tour par tour contre le Basilic avec gestion de probabilités et d'esquives.

#### Répartition des Tâches:
Adrien JULLIAN : input_utils.py,chapitre_1.py et chapitre_5_extension.py, main.py, menu.py
Philéas Eloi : maison.py, personnage.py, chapitre2.py chapitre_3.py, chapitre_4.py

#### Contrôle, Tests et Validation:
Le projet utilise un module dédié input_utils.py pour garantir la stabilité du programme :
    Validation de type : Conversion manuelle des chaînes en entiers pour éviter les plantages.
    Contrôle d'intervalle : Les fonctions vérifient que les choix sont compris dans les bornes autorisées (ex: 1 à 10 pour les attributs).
