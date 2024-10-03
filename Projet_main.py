from Case import Case
from Lemming import Lemming


class jeu():
    def __init__(self, file_path):
        """
        Constructeur de la classe jeu. 
        Initialise la grotte avec une grille de cases et une liste vide pour les lemmings.

        :param grotte: Liste 2D représentant la carte du jeu (grotte), chaque élément est transformé en objet Case.
        """
        # Transformation de chaque élément de la grotte en objet Case
        with open(file_path, 'r') as file:
            lines = file.readlines()
        list_of_lists = [list(line.rstrip('\n')) for line in lines]
        grotte = list_of_lists
        self.grotte =  [[Case(object) for object in ligne] for ligne in grotte]
        self.liste_lemming = []
        self.tour_actuel = 0 
    
    def ajout_lem_entree(self):
        # Ajout d'un premier lemming dans la première ligne de la grotte
        for i in range(len(self.grotte[0])):
            case_actuelle = self.grotte[0][i]
            if case_actuelle.libre():
                Lem = Lemming(0, i, self)  # Crée un nouveau lemming
                self.liste_lemming.append(Lem)  # Ajoute le lemming à la liste
                case_actuelle.arrivee(Lem)  # Place le lemming dans la case
    
    def affiche(self):
        """
        Affiche l'état actuel de la grotte (grille) sur la console.
        Chaque ligne de la grille est affichée séparément.
        """
        for k in range(len(self.grotte)):
            print("")  # Saut de ligne après chaque ligne de la grotte
            for i in range(len(self.grotte[k])):
                # Affiche chaque case de la ligne sans saut de ligne
                print(self.grotte[k][i], end="", sep="")

    def tour(self):
        """
        Fonction placeholder pour gérer le tour d'un lemming ou d'autres événements du jeu.
        À implémenter : déplacements des lemmings et autres interactions.
        """

        if len(self.liste_lemming) > 0:
            self.liste_lemming[self.tour_actuel].action()
            self.tour_actuel += 1
        if len(self.liste_lemming) > 0:
            self.tour_actuel %= len(self.liste_lemming)
            
        print(self.tour_actuel)


    def demarre(self):
        """
        Démarre le jeu et gère la boucle principale de jeu.
        Ajoute un premier lemming dans la première ligne de la grotte si une case est libre, puis continue la boucle de jeu.

        - Affiche la grotte.
        - Demande à l'utilisateur des actions comme ajouter un lemming ou quitter le jeu.
        - Traite chaque tour de jeu.
        """
        
        self.ajout_lem_entree()  # Ajoute un premier lemming dans la grotte

        # Boucle principale du jeu
        est_en_jeu = True
        while est_en_jeu:
            # Affiche l'état actuel de la grotte
            self.affiche()
            # Demande à l'utilisateur ce qu'il veut faire
            action = input("l pour ajouter un lemming, q pour quitter, juste entrer pour continuer: ")
            

            if action == "l":
                if len (self.liste_lemming) == 0:
                    self.tour_actuel = 0
                self.ajout_lem_entree()  # Ajoute un lemming à la liste

            elif action == "q":
                est_en_jeu = False  # Quitte la boucle et termine le jeu

            # Lance le traitement d'un tour (par exemple déplacement des lemmings)
            elif action == "":
                self.tour()
            
            else:
                print("Commande non reconnue, veuillez réessayer.")


# Création d'une instance de jeu avec une grotte (grille) prédéfinie
# jeu = jeu([
#     ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#','#','#'],  # Ligne 1
#     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ', '#'],  # Ligne 2
#     ['#', '#', '#','#','#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],  # Ligne 3
#     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ',' ','#'],  # Ligne 4
#     ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ',' ',' ', '#'],  # Ligne 5
#     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ','0'],  # Ligne 6 (sortie marquée par '0')
#     ['#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#','#','#'],  # Ligne 7
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ',' ',' '],  # Ligne 8
#     [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ',' ',' ']   # Ligne 9
# ])

jeu = jeu("ascii_art_list.txt")

jeu.demarre()
