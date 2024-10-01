class jeu():
    def __init__(self):
        self.__grotte = []

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