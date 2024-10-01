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
