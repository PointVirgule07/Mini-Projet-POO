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
        if self.j.grotte[self.l][self.c].get_terrain() == "0":
            self.sort()
            return
        
        if self.j.grotte[self.l+1][self.c].libre():
            self.j.grotte[self.l][self.c].depart()
            self.j.grotte[self.l+1][self.c].arrivee(self)
            self.l += 1

        elif self.j.grotte[self.l][self.c+self.d].libre():
            self.j.grotte[self.l][self.c].depart()
            self.j.grotte[self.l][self.c+self.d].arrivee(self)
            self.c += self.d

        else:
            self.d *= -1
        
    def sort(self):
        self.j.grotte[self.l][self.c].depart()
        self.j.liste_lemming.pop(self.j.tour_actuel)