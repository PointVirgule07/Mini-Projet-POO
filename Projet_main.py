from Case import Case
from Lemming import Lemming
from generateur import GenerateurLabyrinthe
from random import randint
#sa mère la pute
class Jeu:
    """Classe principale du jeu des lemmings."""

    def __init__(self, largeur, hauteur):
        self.grotte = self.charger_grotte(largeur, hauteur)
        self.liste_lemming = []
        self.tour_actuel = 0

    def charger_grotte(self, largeur, hauteur):
        """Génère une grotte (labyrinthe) avec un générateur au lieu de la charger d'un fichier."""
        generateur = GenerateurLabyrinthe(largeur, hauteur)  # Utilise le générateur de labyrinthe
        labyrinthe = generateur.generer()  # Génère le labyrinthe

        # Conversion du labyrinthe généré en une matrice de Case
        return [[Case(c) for c in ligne] for ligne in labyrinthe]

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
        """Effectue un tour de jeu."""
        if not self.liste_lemming:
            return  # Si aucun lemming, on quitte la méthode.
        
        self.liste_lemming[self.tour_actuel].action()
        self.tour_actuel += 1

        if self.liste_lemming:
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


# Test du jeu avec un labyrinthe généré
largeur = 15
hauteur = 15
jeu = Jeu(largeur, hauteur)
jeu.demarrer()
