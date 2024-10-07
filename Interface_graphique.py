

# class Interface_graphique:

#     def __init__(self):
#         self.fenetre = Tk()
    

#     def affichage(self, tableau):

#         def actualiser_affichage(self):
#             canevas = Canvas(self.fenetre, width=500, height=500)
#             canevas.pack()
#             canevas.delete("all")

#             for i, ligne in enumerate(self.jeu.grotte):
#                 for j, case in enumerate(ligne):
#                     couleur = "white" if case.est_libre() else "black"
#                     canevas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=couleur)
#                     for lemming in case.lemmings:  # si case a des lemmings
#                         canevas.create_oval(j * 20 + 5, i * 20 + 5, j * 20 + 15, i * 20 + 15, fill="green")

#         frame_haut = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
#         frame_milieu = Frame(self.fenetre)

#         titre_principal = Label(frame_haut, text="Lemming", fg="red", font=("Arial", 40))
#         titre_principal.pack()
#         sous_titre = Label(frame_haut, text="Jouer jeu lemming")
#         sous_titre.pack()

#         couleur = {"#": "grey",
#                    " ": "black",
#                    "0": "blue"
#                     }
        
#         pas = 800 / len(tableau)
#         grille = Canvas(self.fenetre) 



#         #parametre de la fenetre
#         self.fenetre.config(bg="#FF00FF")
#         self.fenetre.geometry("500x500")
#         self.fenetre.title("Lemming")
#         self.fenetre.iconbitmap("logo_lemming_game.ico")

        
#         grille.pack()
#         frame_milieu.pack()
#         frame_haut.pack()
from tkinter import *


class Interface_graphique:

    def __init__(self, jeu):
        self.jeu = jeu
        self.fenetre = Tk()
        self.fenetre.title("Jeu des Lemmings")
        self.pas = 30
        self.lemming_image = PhotoImage(file="lemming_image.png")

        self.titre_principal = Label(self.fenetre, text="Lemming")
        # Créer un conteneur pour la disposition
        self.conteneur = Frame(self.fenetre)
        self.conteneur.pack(expand=True, fill=BOTH)

        # Créer le canevas pour afficher la grotte
        self.canevas = Canvas(self.conteneur, bg="white")
        self.canevas.pack(side=LEFT, expand=True, fill=BOTH)

        # Créer le frame pour les boutons
        frame_droite = Frame(self.conteneur)
        frame_droite.pack(side=RIGHT, fill=Y)

        # Ajouter les boutons
        self.bouton_ajouter = Button(frame_droite, text="Ajouter un Lemming", command=self.ajouter_lemming)
        self.bouton_ajouter.pack(pady=5)

        self.bouton_quitter = Button(frame_droite, text="Quitter", command=self.quitter)
        self.bouton_quitter.pack(pady=5)

        self.bouton_changer_tour = Button(frame_droite, text="Changer le mode de tour", command=self.changer_tour, bg="#2aafbb")
        self.bouton_changer_tour.pack(pady=5)

        self.bouton_tour = Button(frame_droite, text="Effectuer le tour", command=self.effectuer_tour)
        self.bouton_tour.pack(pady=5)

        # Mettre à jour la taille de la fenêtre
        self.fenetre.geometry(str(len(self.jeu.grotte[0]) * self.pas + 200) + "x" + str(len(self.jeu.grotte) * self.pas + 100))

        self.actualiser_affichage()
    
    def actualiser_affichage(self):
        couleur = {"#": "black",
                   " ": "white",
                   "0": "green"}

        self.canevas.delete("all") 
        pas = self.canevas.winfo_width() / len(self.jeu.grotte[0])
        for i in range(len(self.jeu.grotte)): 
            ligne = self.jeu.grotte[i] 
            for j in range(len(ligne)): 
                case = ligne[j]   
                self.canevas.create_rectangle(j * pas, i * pas, (j + 1) * pas, (i + 1) * pas, fill=couleur[self.jeu.grotte[i][j].get_terrain()])
                
                if case.lemming != None:
                    if case.lemming.direction == 1:
                        self.canevas.create_arc(j * pas, i * pas, j * pas + 30, i * pas + 20, fill="green", extent=180, start=270)
                    else:
                        self.canevas.create_arc(j * pas, i * pas, j * pas+30, i * pas+20, fill="red", extent=180, start=90)

    def changer_tour(self):
         self.jeu.type_tour *= -1

    def ajouter_lemming(self):
        if len(self.jeu.liste_lemming) == 0:  # Si aucun lemming n'est présent on reset le compteur de tour
            self.jeu.tour_actuel = 0
        self.jeu.ajout_lemming()
        self.actualiser_affichage()

    def effectuer_tour(self):
        self.jeu.tour()
        self.actualiser_affichage()

    def quitter(self):
        self.fenetre.quit()
