class Case:
    """Classe représentant une case du jeu."""

    def __init__(self, terrain, lemming=None):
        self.__terrain = terrain
        self.lemming = lemming

    def __str__(self):
        """Renvoie une représentation de la case."""
        if self.lemming is None:
            return self.__terrain
        else:
            return self.lemming.__str__()

    def get_terrain(self):
        """Renvoie le type de terrain de la case."""
        return self.__terrain

    def est_libre(self):
        """Renvoie True si la case est libre, False sinon."""
        if self.lemming is None and self.__terrain != "#":
            return True
        else:
            return False

    def retirer_lemming(self):
        """Retire le lemming présent dans la case et le renvoie."""
        temp = self.lemming
        self.lemming = None
        return temp

    def ajouter_lemming(self, lemming):
        """Ajoute un lemming à cette case."""
        self.lemming = lemming
