# Import des variables
from variables import *


# Definition de la classe Piece
class Piece(pygame.sprite.Sprite):

    def __init__(self, x, y, nombre):
        pygame.sprite.Sprite.__init__(self)
        self.piece = pygame.Surface((120, 120))
        self.piece.fill(noir)
        self.x = x
        self.y = y
        self.nombre = nombre
        self.affichage_nombre = FONT.render(str(nombre), 1, (blanc))


    def update(self):
        ecran.blit(self.piece, (self.x, self.y))
        ecran.blit(self.affichage_nombre, (self.x + 60, self.y + 60))
       

    def deplacement(self) :


        # Creation des Variables test
        if self.x < 360:
            test_Droite = True
        if self.y > 0:
            test_Haut = True
        if self.y < 360:
            test_Bas = True
        if self.x > 0:
            test_Gauche = True


        # Test si la case a Droite, a Gauche, en Haut ou en Bas est libre
        for i in all_sprites:
            if self.x == 360:
                test_Droite = False
            if self.x + 120 == i.x:
                if self.y == i.y:
                    test_Droite = False
                    break
        for i in all_sprites:
            if self.x == 0:
                test_Gauche = False
            if self.x - 120 == i.x:
                if self.y == i.y:
                    test_Gauche = False
                    break
        for i in all_sprites:
            if self.y == 360:
                test_Bas = False
            if self.y + 120 == i.y:
                if self.x == i.x:
                    test_Bas = False
                    break
        for i in all_sprites:
            if self.y == 0:
                test_Haut = False
            if self.y - 120 == i.y:
                if self.x == i.x:
                    test_Haut = False
                    break


        # Modifie les coordonnees de la piece si il y a un emplacement disponible a cote d'elle
        if self.y > 0:
            if test_Haut == True:
                self.y -= 120
        if self.y < 360:
            if test_Bas == True:
                self.y += 120    
        if self.x > 0:    
            if test_Gauche == True:
                self.x -= 120
        if self.x < 360:
            if test_Droite == True:
                self.x += 120
                
        
# Creation du groupe de sprites "all_sprites"
all_sprites = pygame.sprite.Group()


# Melange automatique des pieces dans le puzzle, attribue au hazard des coordonnees a chaque piece
piece1 = Piece(0, 0, 1)
piece2 = Piece(0, 120, 2)
piece3 = Piece(0, 240, 3)
piece4 = Piece(0, 360, 4)
piece5 = Piece(120, 0, 5)
piece6 = Piece(120, 120, 6)
piece7 = Piece(120, 240, 7)
piece8 = Piece(120, 360, 8)
piece9 = Piece(240, 0, 9)
piece10 = Piece(240, 120, 10)
piece11 = Piece(240, 240, 11)
piece12 = Piece(240, 360, 12)
piece13 = Piece(360, 0, 13)
piece14 = Piece(360, 120, 14)
piece15 = Piece(360, 240, 15)

all_sprites.add(piece1)
all_sprites.add(piece2)
all_sprites.add(piece3)
all_sprites.add(piece4)
all_sprites.add(piece5)
all_sprites.add(piece6)
all_sprites.add(piece7)
all_sprites.add(piece8)
all_sprites.add(piece9)
all_sprites.add(piece10)
all_sprites.add(piece11)
all_sprites.add(piece12)
all_sprites.add(piece13)
all_sprites.add(piece14)
all_sprites.add(piece15)

pieces = [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9, piece10, piece11, piece12, piece13, piece14, piece15]