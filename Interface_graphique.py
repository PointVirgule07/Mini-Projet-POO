from tkinter import *

class Interface_graphique:

    def __init__(self):
        self.fenetre = Tk()
    
    def affichage(self):
        frame_haut = Frame()

        titre_principal = Label(self.fenetre, text="Lemming", fg="red", font=("Arial", 40))
        titre_principal.pack()

        self.fenetre.config(background="#FF00FF")
        self.fenetre.geometry("500x500")
        self.fenetre.mainloop()


interface = Interface_graphique()
interface.affichage()