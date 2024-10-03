class Lemming:
    """Classe représentant un lemming."""

    def __init__(self, ligne, colonne, jeu):
        self.ligne = ligne
        self.colonne = colonne
        self.jeu = jeu
        self.direction = 1  # Direction : 1 pour droite, -1 pour gauche

    def __str__(self):
        """Renvoie une représentation du lemming."""
        if self.direction == 1:
            return ">"
        else:
            return "<"

    def action(self):
        """Effectue l'action du lemming selon sa situation."""
        if self.jeu.grotte[self.ligne][self.colonne].get_terrain() == "0":
            self.sortir()
            return

        if self.jeu.grotte[self.ligne + 1][self.colonne].est_libre():
            self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()
            self.jeu.grotte[self.ligne + 1][self.colonne].ajouter_lemming(self)
            self.ligne += 1
        elif self.jeu.grotte[self.ligne][self.colonne + self.direction].est_libre():
            self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()
            self.colonne += self.direction
            self.jeu.grotte[self.ligne][self.colonne].ajouter_lemming(self)
        else:
            self.direction *= -1

    def sortir(self):
        """Fait sortir le lemming de la grotte."""
        self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()
        self.jeu.liste_lemming.remove(self)
