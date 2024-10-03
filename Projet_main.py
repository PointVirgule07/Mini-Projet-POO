from Case import Case
from Lemming import Lemming

class Jeu:
    """Classe principale du jeu des lemmings."""

    def __init__(self, fichier):
        self.grotte = self.charger_grotte(fichier)
        self.liste_lemming = []
        self.tour_actuel = 0

    def charger_grotte(self, fichier):
        """Charge la grotte à partir d'un fichier texte."""
        with open(fichier, "r") as f:
            return [[Case(c) for c in ligne.strip()] for ligne in f]

    def ajout_lemming(self):
        """Ajoute un lemming à l'entrée de la grotte."""
        for i, case in enumerate(self.grotte[0]):
            if case.est_libre():
                lemming = Lemming(0, i, self)
                case.ajouter_lemming(lemming)
                self.liste_lemming.append(lemming)
                break

    def afficher(self):
        """Affiche la grotte."""
        for ligne in self.grotte:
            print("".join([str(case) for case in ligne]))

    def tour(self):
        """Effectue un tour de jeu tout en évitant les erreurs avec une liste vide."""
        if not self.liste_lemming:
            return  # Si aucun lemming, on quitte la méthode pour éviter toute erreur.

        self.liste_lemming[self.tour_actuel].action() #Effectuer l'action du lemming actuel
        self.tour_actuel += 1

        # S'assurer que tour_actuel reste dans les limites de la liste
        if self.liste_lemming:  # Vérification que la liste n'est pas vide après l'action
            self.tour_actuel %= len(self.liste_lemming)

    def demarrer(self):
        """Démarre la boucle principale du jeu."""
        self.ajout_lemming()
        en_jeu = True

        while en_jeu:
            self.afficher()
            action = input("l pour ajouter un lemming, q pour quitter, entrer pour continuer: ")

            if action == "l":
                if len(self.liste_lemming) == 0:
                    self.tour_actuel = 0
                self.ajout_lemming()
            elif action == "q":
                en_jeu = False
            else:
                self.tour()


# Lancement du jeu
jeu = Jeu("ascii_art_list.txt")
jeu.demarrer()
