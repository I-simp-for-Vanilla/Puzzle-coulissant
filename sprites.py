# Import des variables
from variables import *


# Définition de la classe Pièce
class Pièce(pygame.sprite.Sprite):

    def __init__(self, x, y, nombre):
        pygame.sprite.Sprite.__init__(self)
        self.pièce = pygame.Surface((120, 120))
        self.pièce.fill(noir)
        self.x = x
        self.y = y
        self.nombre = nombre
        self.affichage_nombre = FONT.render(str(nombre), 1, (blanc))


    def update(self):
        ecran.blit(self.pièce, (self.x, self.y))
        ecran.blit(self.affichage_nombre, (self.x + 60, self.y + 60))
       

    def déplacement(self) :


        # Création des Variables test
        if self.x < 360:
            test_Droite = True
        if self.y > 0:
            test_Haut = True
        if self.y < 360:
            test_Bas = True
        if self.x > 0:
            test_Gauche = True


        # Test si la case à Droite, à Gauche, en Haut ou en Bas est libre
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


        # Modifie les coordonnées de la pièce si il y a un emplacement disponible à côté d'elle
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
                
        
# Création du groupe de sprites "all_sprites"
all_sprites = pygame.sprite.Group()


# Mélange automatique des pièces dans le puzzle, attribue au hazard des coordonnées à chaque pièce
pièce1 = Pièce(0, 0, 1)
pièce2 = Pièce(0, 120, 2)
pièce3 = Pièce(0, 240, 3)
pièce4 = Pièce(0, 360, 4)
pièce5 = Pièce(120, 0, 5)
pièce6 = Pièce(120, 120, 6)
pièce7 = Pièce(120, 240, 7)
pièce8 = Pièce(120, 360, 8)
pièce9 = Pièce(240, 0, 9)
pièce10 = Pièce(240, 120, 10)
pièce11 = Pièce(240, 240, 11)
pièce12 = Pièce(240, 360, 12)
pièce13 = Pièce(360, 0, 13)
pièce14 = Pièce(360, 120, 14)
pièce15 = Pièce(360, 240, 15)

all_sprites.add(pièce1)
all_sprites.add(pièce2)
all_sprites.add(pièce3)
all_sprites.add(pièce4)
all_sprites.add(pièce5)
all_sprites.add(pièce6)
all_sprites.add(pièce7)
all_sprites.add(pièce8)
all_sprites.add(pièce9)
all_sprites.add(pièce10)
all_sprites.add(pièce11)
all_sprites.add(pièce12)
all_sprites.add(pièce13)
all_sprites.add(pièce14)
all_sprites.add(pièce15)

pièces = [pièce1, pièce2, pièce3, pièce4, pièce5, pièce6, pièce7, pièce8, pièce9, pièce10, pièce11, pièce12, pièce13, pièce14, pièce15]