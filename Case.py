class Case:
    ''' classe qui désigne une case du jeu.
    Prend en paramètres le type de terrain en chaine de caractère (mur : "▇", vide : " ", sortie : "✿")
    et si un lemming est présent de base ou non, renvoie None s'il la vase est vide.
    '''
  
    def __init__(self, terrain, lemming = None):
        self.__terrain = terrain
        self.__lemming = lemming

    def __str__(self):
        ''' Renvoie une représentation en chaîne de caractères de la case '''
        if self.__lemming is None:
            return self.__terrain
        else:
            return self.__lemming.__str__()
            

    def libre(self):
        ''' Renvoie True si la case est vide et False dans le cas contraire'''
        return self.__lemming == None and (self.__terrain != "#")

    def depart(self):
        ''' Suprimme le lemming present dans la case et le renvoie'''
        temp = self.__lemming 
        self.__lemming = None
        return temp

    def arrivee(self, lem):
        ''' Permet d'ajouter un lemming dans cette case
        Prend en paramètre un lemming et l'associe à cette case
        '''
        self.__lemming = lem