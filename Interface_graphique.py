# Description: Fichier contenant la classe Interface_graphique qui permet de gérer l'interface graphique du jeu des lemmings
from tkinter import *
from PIL import Image, ImageTk

class Interface_graphique:

    def __init__(self, jeu):
        self.jeu = jeu
        self.fenetre = Tk()
        self.fenetre.title("Jeu des Lemmings")
        self.fenetre.iconbitmap("logo_lemming_game.ico")
        # self.fenetre.attributes("-fullscreen", True)  # Ouvrir en plein écran
        self.pas = 70  # Valeur initiale du pas
        
        # Ajouter un attribut pour l'état du mode de tour
        self.mode_tour = 1  # Peut être 1 ou -1

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

        self.bouton_changer_tour = Button(frame_droite, text="Lemming par Lemming", command=self.changer_tour, bg="#2aafbb")
        self.bouton_changer_tour.pack(pady=5)

        self.bouton_tour = Button(frame_droite, text="Effectuer le tour", command=self.effectuer_tour)
        self.bouton_tour.pack(pady=5)

        # Charger les images pour les lemmings
        self.image_droite_base = Image.open("lemming_image__droite.png")
        self.image_gauche_base = Image.open("lemming_image_gauche.png")
    
        # Redimensionner les images selon la taille des cases
        self.image_droite = ImageTk.PhotoImage(self.image_droite_base.resize((self.pas, self.pas)))
        self.image_gauche = ImageTk.PhotoImage(self.image_gauche_base.resize((self.pas, self.pas)))

        # Calculer la taille des cases pour remplir la fenêtre
        self.calculer_taille_cases()  # Initialiser le calcul des cases
        self.actualiser_affichage()  # Afficher initialement la grille

        # Lier l'événement de redimensionnement
        self.fenetre.bind("<Configure>", self.redimensionner)  # Événement de redimensionnement

    def calculer_taille_cases(self):
        """Calculer la taille des cases pour remplir la fenêtre au maximum."""
        # Calculer le nombre de colonnes et de lignes
        nombre_colonnes = len(self.jeu.grotte[0])
        nombre_lignes = len(self.jeu.grotte)

        # Calculer la taille maximale possible pour chaque case
        largeur_fenetre = self.fenetre.winfo_width() - 200  # Ajustement pour les boutons
        hauteur_fenetre = self.fenetre.winfo_height() - 100  # Ajustement pour le titre

        # Assurez-vous que les dimensions de la fenêtre sont positives
        if largeur_fenetre > 0 and hauteur_fenetre > 0:
            # Calculer le pas (taille des cases) pour remplir la fenêtre
            self.pas = min(largeur_fenetre // nombre_colonnes, hauteur_fenetre // nombre_lignes)

            # Redimensionner les images selon la nouvelle taille des cases
            self.image_droite = ImageTk.PhotoImage(self.image_droite_base.resize((self.pas, self.pas)))
            self.image_gauche = ImageTk.PhotoImage(self.image_gauche_base.resize((self.pas, self.pas)))

    def redimensionner(self, event):
        self.calculer_taille_cases()  # Recalculer la taille des cases lors du redimensionnement
        self.actualiser_affichage()  # Mettre à jour l'affichage avec le nouveau pas

    def actualiser_affichage(self):
        couleur = {"#": "black",
                   " ": "white",
                   "0": "green"}

        self.canevas.delete("all") 
        pas = self.pas  # Utiliser le pas calculé
        for i in range(len(self.jeu.grotte)): 
            ligne = self.jeu.grotte[i] 
            for j in range(len(ligne)): 
                case = ligne[j]   
                self.canevas.create_rectangle(j * pas, i * pas, (j + 1) * pas, (i + 1) * pas, fill=couleur[self.jeu.grotte[i][j].get_terrain()])
                
                if case.lemming != None:
                    if case.lemming.direction == 1:
                        # Calculer la position centrée
                        x_position = j * pas + (pas // 2)  # Décalage pour centrer horizontalement
                        y_position = i * pas + (pas // 2)  # Décalage pour centrer verticalement
                        # Afficher l'image pour le lemming allant à droite
                        self.canevas.create_image(x_position, y_position, anchor="center", image=self.image_droite)
                    else:
                        # Calculer la position centrée
                        x_position = j * pas + (pas // 2)  # Décalage pour centrer horizontalement
                        y_position = i * pas + (pas // 2)  # Décalage pour centrer verticalement
                        # Afficher l'image pour le lemming allant à gauche
                        self.canevas.create_image(x_position, y_position, anchor="center", image=self.image_gauche)

    def changer_tour(self):
        self.jeu.type_tour *= -1
        # Changer le texte du bouton selon le mode actuel
        if self.jeu.type_tour == 1:
            self.bouton_changer_tour.config(text="Lemming par Lemming")
        else:
            self.bouton_changer_tour.config(text="Tous les Lemmings en même temps")

    def ajouter_lemming(self):
        if len(self.jeu.liste_lemming) == 0:  # Si aucun lemming n'est présent on reset le compteur de tour
            self.jeu.tour_actuel = 0
        self.jeu.ajout_lemming()
        self.actualiser_affichage()

    def effectuer_tour(self):
        self.jeu.tour()
        self.actualiser_affichage()

    def quitter(self):
        self.jeu.en_jeu = False
        self.fenetre.quit()
