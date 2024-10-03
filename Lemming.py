from Jeu import Jeu

class Lemming():
    """Cette classe gère le comportement des lemmings dans le jeu"""
    def __init__(self, l, c, j):
        self.l = l
        self.c = c
        self.j = j
        self.d = 1
    
    def __str__(self):   
        return ">" if self.d == 1 else "<"
    
    def action(self):
        if Jeu.grotte[self.l+1][self.c].libre():
            Jeu.grotte[self.l][self.c].depart()
            Jeu.grotte[self.l+1][self.c].arrivee(self.)
            self.l += 1

        elif Jeu.grotte[self.l][self.c+self.d].libre():
            Jeu.grotte[self.l][self.c].depart()
            Jeu.grotte[self.l][self.c+self.d].arrivee(self)
            self.c += self.d

        else:
            self.d *= -1
        
    def sort(self):
        case.depart()
        Jeu.liste_lemming.pop(Jeu.tour_actuel)