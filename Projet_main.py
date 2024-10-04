from Case import Case
from Lemming import Lemming

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

    def charger_grotte(self, fichier):
        """Charge la grotte à partir d'un fichier texte."""
        with open(fichier, "r") as f:
            return [[Case(c) for c in ligne.strip()] for ligne in f] #converti chaque caractère en objet Case

    def ajout_lemming(self):
        """Ajoute un lemming à l'entrée de la grotte."""
        for i, case in enumerate(self.grotte[0]):
            if case.est_libre():
                lemming = Lemming(0, i, self)
                case.ajouter_lemming(lemming)
                self.liste_lemming.append(lemming)
                return

    def afficher(self):
        """Affiche la grotte."""
        for ligne in self.grotte:
            # Affiche chaque ligne en concaténant les représentations des cases
            print("".join([str(case) for case in ligne]))

    def tour_par_tour(self):
        """Effectue un tour de jeu tout en évitant les erreurs avec une liste vide."""
        if not self.liste_lemming:
            return  # Si aucun lemming, on quitte la méthode pour éviter toute erreur.

        self.liste_lemming[self.tour_actuel].action() # Effectue l'action du lemming actuel
        self.tour_actuel += 1

        # S'assurer que tour_actuel reste dans les limites de la liste
        if self.liste_lemming:  # Vérification que la liste n'est pas vide après l'action
            self.tour_actuel %= len(self.liste_lemming)  # Réinitialise tour_actuel si nécessaire

    def tour(self):
        '''self.type_tour = 0 pour un tour par tour et 1 pour tous en meme temps
        '''
        if self.type_tour == 1:
            self.tour_par_tour()
        elif self.type_tour == -1:
            for i in range(len(self.liste_lemming)):
                self.tour_par_tour()


    def alterner(self, comment):
        ''' 0 pour un tour par tour et 1 pour tous en meme temps
        '''


    def demarrer(self):
        """Démarre la boucle principale du jeu."""
        
        self.ajout_lemming()  # Ajoute le premier lemming à la grotte
        en_jeu = True  # État du jeu

        while en_jeu:
            self.afficher()  # Affiche l'état actuel de la grotte
            action = input("l pour ajouter un lemming, q pour quitter, entrer pour continuer: ")

            if action == "l":

                if len(self.liste_lemming) == 0:# Si aucun lemming n'est présent on reset le compteur de tour pour ne pas out of range
                    self.tour_actuel = 0

                self.ajout_lemming()

            elif action == "q": # Quitte le jeu
                en_jeu = False
            
            elif action == "c": # Change le type de passage des tour
                self.type_tour *= -1 

            else:
                self.tour()  # Effectue le tour de jeu pour le lemming actuel
                


# Lancement du jeu
jeu = Jeu("ascii_art_list.txt")  # Initialise le jeu avec le fichier de grotte
jeu.demarrer()  # Démarre le jeu