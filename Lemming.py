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
        pass

    def sort(self):
        pass