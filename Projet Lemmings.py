class Case:
    ''' classe qui désigne une case du jeu.
    Prend en paramètres le type de terrain en chaine de caractère (mur, vide, sortie)
    et si un lemming est présent de base ou non, renvoie None s'il la vase est vide.
    '''
  
    def __init__(self, terrain, lemming = None):
        self.terrain = terrain
        self.lemming = lemming

    def __self__(self):
        if self.terrain == "mur":
            return "▇"
        elif self.terrain == "vide":
            return " "
        elif self.terrain == "sortie":
            return "✿"

    def libre(self):
        ''' Renvoie True si la case est vide et False dans le cas contraire
        '''
        return self.lemming == None and (self.terrain == "vide" or self.terrain == "sortie")

    def depart(self):
        ''' Suprimme le lemming present dans la case et le renvoie
        '''
        temp = self.lemming 
        self.lemming = None
        return temp

    def arrivee(self, lem):
        ''' Permet d'ajouter un lemming dans cette case
        Prend en paramètre un lemming et l'associe à cette case
        '''
        self.lemming = lem
