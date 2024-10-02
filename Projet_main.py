from Case import Case
from Lemming import Lemming

class jeu():

    def __init__(self, grotte):
        """
        Constructeur de la classe jeu. 
        Initialise la grotte avec une grille de cases et une liste vide pour les lemmings.

        :param grotte: Liste 2D représentant la carte du jeu (grotte), chaque élément est transformé en objet Case.
        """
        # Transformation de chaque élément de la grotte en objet Case
        self.__grotte =  [[Case(object) for object in ligne] for ligne in grotte]
        # Liste pour stocker les lemmings
        self.liste_lemming = []

    def affiche(self):
        """
        Affiche l'état actuel de la grotte (grille) sur la console.
        Chaque ligne de la grille est affichée séparément.
        """
        for k in range(len(self.__grotte)):
            print("")  # Saut de ligne après chaque ligne de la grotte
            for i in range(len(self.__grotte[k])):
                # Affiche chaque case de la ligne sans saut de ligne
                print(self.__grotte[k][i], end="", sep="")

    def tour(self):
        """
        Fonction placeholder pour gérer le tour d'un lemming ou d'autres événements du jeu.
        À implémenter : déplacements des lemmings et autres interactions.
        """
        pass  # Le contenu de cette méthode est à implémenter plus tard

    def demarre(self):
        """
        Démarre le jeu et gère la boucle principale de jeu.
        Ajoute un premier lemming dans la première ligne de la grotte si une case est libre, puis continue la boucle de jeu.

        - Affiche la grotte.
        - Demande à l'utilisateur des actions comme ajouter un lemming ou quitter le jeu.
        - Traite chaque tour de jeu.
        """
        
        # Ajout d'un premier lemming dans la première ligne de la grotte
        for i in range(len(self.__grotte[0])):
            case_actuelle = self.__grotte[0][i]
            if case_actuelle.libre():
                Lem = Lemming(0, i, self)  # Crée un nouveau lemming
                self.liste_lemming.append(Lem)  # Ajoute le lemming à la liste
                case_actuelle.arrivee(Lem)  # Place le lemming dans la case
                break  # Arrête l'ajout une fois un lemming placé 

        # Boucle principale du jeu
        while True:
            # Affiche l'état actuel de la grotte
            self.affiche()

            # Demande à l'utilisateur ce qu'il veut faire
            action = input("l pour ajouter un lemming, q pour quitter, juste entrer pour continuer: ")

            if action == "l":
                # Placeholder pour ajouter un nouveau lemming (à implémenter)
                pass

            elif action == "q":
                break  # Quitte la boucle et termine le jeu

            # Lance le traitement d'un tour (par exemple déplacement des lemmings)
            self.tour()


# Création d'une instance de jeu avec une grotte (grille) prédéfinie
jeu = jeu([
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#','#','#'],  # Ligne 1
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ', '#'],  # Ligne 2
    ['#', '#', '#','#','#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],  # Ligne 3
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ',' ','#'],  # Ligne 4
    ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ',' ',' ', '#'],  # Ligne 5
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ','0'],  # Ligne 6 (sortie marquée par '0')
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#','#','#'],  # Ligne 7
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ',' ',' '],  # Ligne 8
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ',' ',' ']   # Ligne 9
])

# Démarrage du jeu
jeu.demarre()
