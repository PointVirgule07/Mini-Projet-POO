class Lemming:
    """
    Classe représentant un lemming.

    Un lemming se déplace dans une grotte selon des règles simples :
    - Il avance dans une direction donnée (droite ou gauche).
    - Il tombe s'il y a un espace libre en dessous.
    - Il change de direction s'il rencontre un obstacle.
    - Il sort de la grotte lorsqu'il atteint la sortie.
    
    Attributs :
    - ligne : la position du lemming sur l'axe vertical (ligne).
    - colonne : la position du lemming sur l'axe horizontal (colonne).
    - jeu : une référence à l'objet jeu pour accéder aux méthodes et à la grotte.
    - direction : indique la direction du lemming (1 pour droite, -1 pour gauche).
    """

    def __init__(self, ligne, colonne, jeu):
        self.ligne = ligne
        self.colonne = colonne
        self.jeu = jeu
        self.direction = 1

    def __str__(self):
        """Renvoie une représentation visuelle du lemming."""
        if self.direction == 1:
            return "\033[31m>\033[37m"
        else:
            return "\033[31m<\033[37m"

    def action(self):
        """Effectue l'action du lemming selon sa situation dans la grotte."""
        # Si le lemming est sur une case de sortie ('0'), il sort de la grotte.
        if self.jeu.grotte[self.ligne][self.colonne].get_terrain() == "0":
            self.sortir()
            return

        # Vérifie si la case en dessous du lemming est libre (lemming tombe)
        if self.jeu.grotte[self.ligne + 1][self.colonne].est_libre():
            self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()  # Retirer de l'ancienne case
            self.jeu.grotte[self.ligne + 1][self.colonne].ajouter_lemming(self)  # Ajouter à la nouvelle case
            self.ligne += 1  # Mise à jour de la position (le lemming descend)
        
        # Si la case devant le lemming dans la direction actuelle est libre
        elif self.jeu.grotte[self.ligne][self.colonne + self.direction].est_libre():
            self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()  # Retirer de l'ancienne case
            self.colonne += self.direction  # Avance dans la direction actuelle
            self.jeu.grotte[self.ligne][self.colonne].ajouter_lemming(self)  # Ajouter à la nouvelle case
        
        # Si la case devant est bloquée, changer de direction
        else:
            self.direction *= -1  # Inversion de la direction

    def sortir(self):
        """Retire le lemming de sa position actuelle et de la liste des lemmings du jeu"""
        self.jeu.grotte[self.ligne][self.colonne].retirer_lemming()
        self.jeu.liste_lemming.remove(self)
