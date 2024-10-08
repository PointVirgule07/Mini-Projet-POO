# Description: Fichier contenant la classe Interface_graphique qui permet de gérer l'interface graphique du jeu des lemmings
from tkinter import *
from PIL import Image, ImageTk
import pygame
from random import choice

class Interface_graphique:

    def __init__(self, jeu):
        self.jeu = jeu
        self.fenetre = Tk()
        self.fenetre.title("Jeu des Lemmings")
        self.fenetre.iconbitmap("ressources/images/logo_lemming_game.ico")
        self.fenetre.geometry("800x600")
        self.fenetre.minsize(400, 300)

        # Lancer la musique de fond
        self.lancer_musique()

        # self.fenetre.attributes("-fullscreen", True)  # Ouvrir en plein écran
        self.pas = 70
        
        # Attribut pour l'écran d'accueil
        self.ecran_accueil = Frame(self.fenetre)
        self.ecran_accueil.pack(expand=True, fill=BOTH)

        # Ajouter une image sur l'écran d'accueil
        image_accueil = Image.open("ressources/images/logo_lemming_game.ico")  # Assurez-vous que cette image existe
        image_accueil = ImageTk.PhotoImage(image_accueil.resize((400, 300)))  # Redimensionner selon votre besoin

        self.label_image = Label(self.ecran_accueil, image=image_accueil)
        self.label_image.image = image_accueil  # Nécessaire pour éviter la collecte du garbage
        self.label_image.pack(pady=50)

        # Ajouter un bouton "Jouer" sur l'écran d'accueil
        self.bouton_jouer = Button(self.ecran_accueil, text="Jouer", command=self.lancer_jeu, font=("Arial", 16), bg="green", fg="white")
        self.bouton_jouer.pack(pady=20)

        # Ajouter un attribut pour l'état du mode de tour
        self.mode_tour = 1

        # Créer un conteneur pour la disposition
        self.conteneur = Frame(self.fenetre)

        # Créer le canevas pour afficher la grotte
        self.canevas = Canvas(self.conteneur, bg="white")

        # Créer le frame pour les boutons
        frame_droite = Frame(self.conteneur)
        frame_droite.pack(side=RIGHT, fill=Y)

        # Ajouter les bouton
        self.bouton_quitter = Button(frame_droite, text="Quitter", command=self.quitter, bg="#ff0000")
        self.bouton_quitter.pack(pady=5)

        self.bouton_changer_tour = Button(frame_droite, text="Lemming par Lemming", command=self.changer_tour, bg="#2aafbb")
        self.bouton_changer_tour.pack(pady=5)
        
        self.bouton_ajouter = Button(frame_droite, text="Ajouter un Lemming", command=self.ajouter_lemming)
        self.bouton_ajouter.pack(pady=5)

        self.bouton_tour = Button(frame_droite, text="Effectuer le tour", command=self.effectuer_tour)
        self.bouton_tour.pack(pady=5)

        # Charger les images pour les lemmings
        self.image_droite_base = Image.open("ressources/images/lemming_image__droite.png")
        self.image_gauche_base = Image.open("ressources/images/lemming_image_gauche.png")
    
        # Redimensionner les images selon la taille des cases
        self.image_droite = ImageTk.PhotoImage(self.image_droite_base.resize((self.pas, self.pas)))
        self.image_gauche = ImageTk.PhotoImage(self.image_gauche_base.resize((self.pas, self.pas)))

        # Calculer la taille des cases pour remplir la fenêtre
        self.calculer_taille_cases()
        self.actualiser_affichage()

        # Lier l'événement de redimensionnement
        self.fenetre.bind("<Configure>", self.redimensionner)  # Lier la méthode redimensionner à l'événement de redimensionnement de la fenêtre
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quitter)  # Lier la méthode quitter à l'événement de fermeture de la fenêtre
    
    def lancer_musique(self):
        try:
                pygame.mixer.init()
                # Charger la musique et la jouer en boucle
                lib=["ressources/musique/1.mp3","ressources/musique/2.mp3","ressources/musique/3.mp3","ressources/musique/4.mp3","ressources/musique/5.mp3","ressources/musique/6.mp3","ressources/musique/7.mp3"]
                pygame.mixer.music.load(choice(lib))  # Charger le fichier de musique
                pygame.mixer.music.play()
                for _ in range(10):
                    pygame.mixer.music.queue(choice(lib))

            except pygame.error as e:
                print(f"Erreur lors du chargement de la musique : {e}")
            except FileNotFoundError:
                print("Fichier audio non trouvé. Assurez-vous que les fichiers de musique existent.")
            except Exception as e:
                print(f"Une erreur inattendue s'est produite : {e}")

    def lancer_jeu(self):
            """Cache l'écran d'accueil et lance l'interface du jeu."""
            self.ecran_accueil.pack_forget()  # Masquer l'écran d'accueil

            # Afficher le conteneur principal (canevas + boutons)
            self.conteneur.pack(expand=True, fill=BOTH)
            self.canevas.pack(side=LEFT, expand=True, fill=BOTH)

            self.fenetre.focus_set()  # Assurer que la fenêtre a le focus
            self.fenetre.bind("<space>", lambda event: self.effectuer_tour())  # Bouge les lemmings avec la barre espace

            self.actualiser_affichage()

    def calculer_taille_cases(self):
        """Calculer la taille des cases pour remplir la fenêtre au maximum."""
        # Calculer le nombre de colonnes et de lignes
        nombre_colonnes = len(self.jeu.grotte[0])  # Nombre de colonnes dans la grotte (basé sur la longueur de la première ligne)
        nombre_lignes = len(self.jeu.grotte)  # Nombre de lignes dans la grotte

        # Calculer la taille maximale possible pour chaque case
        largeur_fenetre = self.fenetre.winfo_width() - 200  # Ajustement pour l'espace occupé par les boutons à droite
        hauteur_fenetre = self.fenetre.winfo_height() - 100  # Ajustement pour l'espace occupé par le titre en haut

        # Assurez-vous que les dimensions de la fenêtre sont positives
        if largeur_fenetre > 0 and hauteur_fenetre > 0:
            # Calculer le pas (taille des cases) pour remplir la fenêtre
            self.pas = min(largeur_fenetre // nombre_colonnes, hauteur_fenetre // nombre_lignes)  # Trouver la taille maximale des cases pour tout faire rentrer

            # Redimensionner les images selon la nouvelle taille des cases
            self.image_droite = ImageTk.PhotoImage(self.image_droite_base.resize((self.pas, self.pas)))  # Adapter l'image droite à la nouvelle taille de case
            self.image_gauche = ImageTk.PhotoImage(self.image_gauche_base.resize((self.pas, self.pas)))  # Adapter l'image gauche à la nouvelle taille de case

    def redimensionner(self, event):
        self.calculer_taille_cases() # Recalculer la taille des cases lors du redimensionnement
        self.actualiser_affichage()

    def actualiser_affichage(self):

        couleur = {"#": "black",
                   " ": "white",
                   "0": "green"}

        self.canevas.delete("all")  # Effacer le contenu du canevas avant de redessiner
        pas = self.pas
        for i in range(len(self.jeu.grotte)): 
            ligne = self.jeu.grotte[i]  # Obtenir la ligne courante
            for j in range(len(ligne)): 
                case = ligne[j]
                # Créer un rectangle coloré pour chaque case selon son type de terrain
                self.canevas.create_rectangle(j * pas, i * pas, (j + 1) * pas, (i + 1) * pas, fill=couleur[self.jeu.grotte[i][j].get_terrain()])
                
                if case.lemming != None:
                    if case.lemming.direction == 1:

                        # Calculer la position centrée
                        x_position = j * pas + (pas // 2)
                        y_position = i * pas + (pas // 2)
                        self.canevas.create_image(x_position, y_position, anchor="center", image=self.image_droite)

                    else:
                        # Calculer la position centrée
                        x_position = j * pas + (pas // 2)
                        y_position = i * pas + (pas // 2)
                        self.canevas.create_image(x_position, y_position, anchor="center", image=self.image_gauche)

    def changer_tour(self):
        self.jeu.type_tour *= -1  # Inverser le type de tour (1 ou -1)

        # Changer le texte du bouton selon le mode actuel
        if self.jeu.type_tour == 1:
            self.bouton_changer_tour.config(text="Lemming par Lemming")
        else:
            self.bouton_changer_tour.config(text="Tous les Lemmings en même temps")

    def ajouter_lemming(self):
        if len(self.jeu.liste_lemming) == 0:
            self.jeu.tour_actuel = 0
        self.jeu.ajout_lemming()
        self.actualiser_affichage()

    def effectuer_tour(self):
        self.jeu.tour()
        self.actualiser_affichage()

    def quitter(self):
        self.jeu.en_jeu = False
        self.fenetre.quit()
