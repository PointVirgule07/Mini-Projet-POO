from tkinter import *

class Interface_graphique:

    def __init__(self):
        self.fenetre = Tk()
    
    def afficher_grille(self, tableau):
        for ligne in range(len(tableau)):
            for colon,e in range(len(tableau[0])):
                pass


    def affichage(self):
        frame_haut = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        frame_millieu = Frame(self.fenetre)

        titre_principal = Label(frame_haut, text="Lemming", fg="red", font=("Arial", 40))
        titre_principal.pack()
        sous_titre = Label(frame_haut, text="Jouer jeu lemming")
        sous_titre.pack()


        self.fenetre.config(background="#FF00FF")
        self.fenetre.geometry("500x500")

        frame_miilieu.pack()
        frame_haut.pack()
        self.fenetre.mainloop()


interface = Interface_graphique()
interface.affichage()