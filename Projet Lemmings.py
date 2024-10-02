class Case:
    ''' classe qui désigne une case du jeu.
    Prend en paramètres le type de terrain en chaine de caractère (mur : "▇", vide : " ", sortie : "✿")
    et si un lemming est présent de base ou non, renvoie None s'il la vase est vide.
    '''
  
    def __init__(self, terrain, lemming = None):
        self.terrain = terrain
        self.lemming = lemming

    def __str__(self):
        if self.lemming == None: 
            return self.terrain
        else:
            print(self.lemming)

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

class Lemming():
    """Cette classe gère le comportement des lemmings dans le jeu"""
    def __init__(self):
        self.l = 0
        self.c = 0
        self.d = 1
    
    def __str__(self):   
        return ">" if self.d == 1 else "<"
    
    def action(self):
        pass

    def sort(self):
        pass


class jeu():
    """Cette classe gère le jeu"""
    def __init__(self, grotte):
        self.__grotte = grotte

    def affiche(self):
        for i in range(len(self.__grotte)):
            print(self.__grotte[i])
    
    def tour(self):
        pass #chai pas quoi faire encore

    def demarre(self):
        while True:
            action = input("l pour ajouter un lemming, q pour quitter, juste entrer pour continuer")
            
            if action == "l":
                #ajouter un lemming
                pass

            elif action == "q":
                break 

            self.tour()
            self.affiche()
