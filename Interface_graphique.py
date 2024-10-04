from tkinter import *

class Interface_graphique:

    def __init__(self):
        self.fenetre = Tk()
    


    def affichage(self, tableau):
        frame_haut = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        frame_milieu = Frame(self.fenetre)

        titre_principal = Label(frame_haut, text="Lemming", fg="red", font=("Arial", 40))
        titre_principal.pack()
        sous_titre = Label(frame_haut, text="Jouer jeu lemming")
        sous_titre.pack()

        couleur = ["grey", "red", "red", "grey", "red"]
        pas = 800 / len(tableau)
        grille = Canvas(self.fenetre) 

        for ligne in range(len(tableau)):
            for colone in range(len(tableau[0])):
                x1, y1 = pas * colone, pas * ligne
                x2, y2 = pas * (colone), pas * (ligne)
                grille.create_rectangle(x1, y1, x2, y2, fill=couleur[ligne])


        self.fenetre.config(background="#FF00FF")
        self.fenetre.geometry("500x500")

        grille.pack()
        frame_milieu.pack()
        frame_haut.pack()
        self.fenetre.mainloop()


interface = Interface_graphique()
interface.affichage(
    [
    ["#", "#"],
    ["#", "#"]
    ])