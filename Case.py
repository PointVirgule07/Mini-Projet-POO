class Case:
    """
    Classe représentant une case du jeu.

    Chaque case peut contenir un terrain (ex : mur, espace libre, sortie)
    et éventuellement un lemming. Elle gère les interactions avec le lemming
    qui se déplace sur elle.

    Attributs :
    - terrain : le type de terrain de la case (ex: '#', '.', '0').
    - lemming : une référence au lemming qui occupe la case (None si vide).
    """

    def __init__(self, terrain, lemming=None):
        self.__terrain = terrain  # Type de terrain de la case
        self.lemming = lemming  # Référence au lemming, None par défaut

    def __str__(self):
        """Renvoie une représentation de la case."""
        if self.lemming is None:
            return self.__terrain  # Renvoie le symbole du terrain si pas de lemming
        else:
            return self.lemming.__str__()  # Renvoie la représentation du lemming

    def get_terrain(self):
        """Renvoie le type de terrain de la case."""
        return self.__terrain  # Retourne le type de terrain (mur, libre, sortie)

    def est_libre(self):
        """Renvoie True si la case est libre, False sinon."""
        return self.lemming is None and self.__terrain != "#"

    def retirer_lemming(self):
        """Retire le lemming présent dans la case et le renvoie."""
        temp = self.lemming  # Stocke temporairement le lemming
        self.lemming = None  # Retire le lemming de la case
        return temp  # Retourne le lemming retiré

    def ajouter_lemming(self, lemming):
        """Ajoute un lemming à cette case."""
        self.lemming = lemming
