import random

class GenerateurLabyrinthe:
    """Classe pour générer un labyrinthe compatible avec les comportements des lemmings."""
    
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.labyrinthe = [["#" for _ in range(largeur)] for _ in range(hauteur)]

    def voisins(self, x, y):
        """Renvoie la liste des voisins possibles pour creuser."""
        voisins_possibles = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Haut, Bas, Gauche, Droite
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.hauteur - 1 and 1 <= ny < self.largeur - 1:
                if self.labyrinthe[nx][ny] == "#":
                    voisins_possibles.append((nx, ny))
        return voisins_possibles

    def creuser(self, x, y):
        """Creuse un chemin en partant de la position (x, y)."""
        self.labyrinthe[x][y] = " "  # Marquer la cellule comme libre
        voisins = self.voisins(x, y)
        random.shuffle(voisins)
        for (nx, ny) in voisins:
            if self.labyrinthe[nx][ny] == "#":
                # Creuser entre la cellule actuelle et le voisin
                self.labyrinthe[(x + nx) // 2][(y + ny) // 2] = " "
                self.creuser(nx, ny)

    def generer(self):
        """Génère un labyrinthe avec une entrée et une sortie."""
        # Initialiser avec une entrée aléatoire
        entree_x = 0
        entree_y = random.randint(1, self.largeur - 2)
        self.labyrinthe[entree_x][entree_y] = " "

        # Creuser à partir de l'entrée
        self.creuser(1, entree_y)

        # Ajouter une sortie en bas
        sortie_x = self.hauteur - 1
        sortie_y = random.randint(1, self.largeur - 2)
        self.labyrinthe[sortie_x][sortie_y] = "0"

        return self.labyrinthe

    def afficher(self):
        """Affiche le labyrinthe généré."""
        for ligne in self.labyrinthe:
            print("".join(ligne))

