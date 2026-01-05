# Poudelard : L'Aventure Magique

#### Description :
Jeu de rôle textuel développé en Python où le joueur incarne un jeune sorcier.
Le jeu suit une progression en 5 chapitres : de l'achat des fournitures 
sur le Chemin de Traverse jusqu'au combat final dans la Chambre des Secrets.

#### Contributeurs :
Adrien JULLIAN - Philéas ELOI

#### Installation :
1. Cloner le dépôt : `git clone https://github.com/yoshiijoe/poudelard-Eloi-Jullian-PP.git`
2. Ouvrir le dossier `poudelard` dans votre IDE (PyCharm recommandé).

#### Utilisation :
Pour lancer le jeu, exécutez le fichier `main.py` à la racine du projet. 
*Note : Assurez-vous que le "Working Directory" est configuré sur la racine du projet.*

#### Fonctionnalités Principales :
- **Création de personnage** : Attributs personnalisables (courage, intelligence, loyauté, ambition).
- **Gestion d'inventaire** : Achat dynamique via des fichiers de données JSON.
- **Cérémonie de Répartition** : Algorithme déterminant la maison selon les choix du joueur.
- **Système de Combat** : Duel tour par tour contre le Basilic (gestion probabilités/esquives).
- **Exportation** : Génération d'un certificat de fin d'année en `.txt`.

#### Journal de Bord :
**Chronologie :**
- Décembre 2025 : Initialisation du projet et création du module de saisie sécurisée.
- Fin décembre 2025 : Développement des chapitres narratifs et du système de Quidditch.
- Janvier 2026 : Finalisation du combat final, du menu principal et nettoyage du code.

**Répartition des Tâches :**
- **Adrien JULLIAN** : `input_utils.py`, `chapitre_1.py`, `chapitre_5.py`, `main.py`, `menu.py`, `export_utils.py`.
- **Philéas ELOI** : `maison.py`, `personnage.py`, `chapitre_2.py`, `chapitre_3.py`, `chapitre_4.py`.

#### Contrôle, Tests et Validation :
Le projet utilise un module dédié `input_utils.py` pour garantir la stabilité du programme :
- **Validation de type** : Conversion manuelle des chaînes en entiers pour éviter les plantages.
- **Contrôle d'intervalle** : Vérification des bornes autorisées (ex: 1 à 10 pour les attributs).

**Bugs connus :**
- L'affichage des emojis peut varier selon l'encodage du terminal utilisé (UTF-8 requis).
- Nécessité de configurer manuellement le chemin d'exécution sur certains IDE pour accéder aux dossiers `data/`.

#### Stratégies de Test :
- **Tests de saisie** : Vérification de la résistance aux entrées incorrectes (lettres à la place de chiffres).
- **Tests de logique** : Validation de l'attribution des points de maison et de la sélection du Choixpeau.
- **Équilibrage** : Tests statistiques sur le combat final pour garantir un défi équitable.

![Capture du menu](img_1.png)
![Capture du combat](img.png)
![Capture de l'export](img_2.png)