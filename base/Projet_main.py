from Case import Case
from Lemming import Lemming
from Interface_graphique import Interface_graphique

class Jeu:
    """
    Classe principale du jeu des lemmings.
    
    Gère la création et l'affichage de la grotte, ainsi que les interactions
    avec les lemmings. Permet d'ajouter des lemmings, d'effectuer des tours
    de jeu et d'afficher l'état actuel de la grotte.

    Attributs :
    - grotte : une matrice représentant le terrain du jeu, chaque case étant un objet Case.
    - liste_lemming : une liste de tous les lemmings présents dans le jeu.
    - tour_actuel : un compteur pour suivre quel lemming doit agir au prochain tour.
    """

    def __init__(self, fichier):
        self.grotte = self.charger_grotte(fichier)  # Charge la grotte à partir d'un fichier
        self.liste_lemming = []
        self.tour_actuel = 0
        self.type_tour = 1
        self.en_jeu = None

    def charger_grotte(self, fichier):
        """Charge la grotte à partir d'un fichier texte."""
        with open(fichier, "r") as f:
            return [[Case(c) for c in ligne.strip()] for ligne in f] #converti chaque caractère en objet Case
            # .strip() enlève les espaces, tabulations et retours à la ligne en début et fin de chaque ligne
            # Cela permet de ne garder que les caractères « significatifs » de la ligne.


    def ajout_lemming(self):
        """Ajoute un lemming à l'entrée de la grotte."""
        for i in range(len(self.grotte[0])):
            case = self.grotte[0][i] # Récupère la ième case à la première ligne
            if case.est_libre(): # Si la case est libre, ajoute un lemming
                lemming = Lemming(0, i, self) 
                case.ajouter_lemming(lemming) 
                self.liste_lemming.append(lemming) 
                return # Sort de la méthode après avoir ajouté un lemming

    def afficher(self):
        """
        Affiche l'état actuel de la grotte (grille) sur la console.
        Chaque ligne de la grille est affichée séparément.
        """
        for k in range(len(self.grotte)):
            print("")  # Saut de ligne après chaque ligne de la grotte
            for i in range(len(self.grotte[k])):
                # Affiche chaque case de la ligne sans saut de ligne
                print(self.grotte[k][i], end="", sep="")

    def tour_par_tour(self):
        """Effectue un tour de jeu tout en évitant les erreurs avec une liste vide."""
        if self.liste_lemming == []:
            return  # Si aucun lemming, on quitte la méthode pour éviter toute erreur.
        self.liste_lemming[self.tour_actuel].action() # Effectue l'action du lemming actuel
        self.tour_actuel += 1

        # S'assurer que tour_actuel reste dans les limites de la liste
        if self.liste_lemming != []:  # Vérification que la liste n'est pas vide après l'action
            self.tour_actuel %= len(self.liste_lemming)  # Réinitialise tour_actuel si nécessaire

    def tour(self):
        '''self.type_tour = 0 pour un tour par tour et 1 pour tous en meme temps
        '''
        if self.type_tour == 1:
            self.tour_par_tour()
        elif self.type_tour == -1:
            for i in range(len(self.liste_lemming)):
                self.tour_par_tour()


    def demarrer(self):
        """Démarre la boucle principale du jeu."""
        
        self.ajout_lemming()  # Ajoute le premier lemming à la grotte
        self.en_jeu = True  # État du jeu

        interface = Interface_graphique(self)
        interface.fenetre.mainloop()

        while self.en_jeu:
            self.afficher()  # Affiche l'état actuel de la grotte
            action = input("l pour ajouter un lemming, q pour quitter, entrer pour continuer: ")

            if action == "l":

                if len(self.liste_lemming) == 0:# Si aucun lemming n'est présent on reset le compteur de tour pour ne pas out of range
                    self.tour_actuel = 0

                self.ajout_lemming()

            elif action == "q": # Quitte le jeu
                self.en_jeu = False
            
            elif action == "c": # Change le type de passage des tour
                self.type_tour *= -1 

            elif action == "":
                self.tour()  # Effectue le tour de jeu pour le lemming actuel
            
            else:
                print("\033[31mCommande invalide\033[37m")
                


# Lancement du jeu
jeu = Jeu("map_asci.txt")  # Initialise le jeu avec le fichier de grotte
jeu.demarrer()  # Démarre le jeu