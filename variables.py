# Import des modules
import pygame, sys
from random import randint
pygame.init()


# Définition de la variable de jeu
arret_jeu = False


# Affichage de l'écran
ecran = pygame.display.set_mode((480, 480))


# Définition du nom de la fenêtre
pygame.display.set_caption("Puzzle coulissant")


# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)


# Font
FONT = pygame.font.Font(None, 24)


# Définition des variables liées au mélange des pièces
coordonnées2 = [(0, 0), (120, 0), (240, 0), (360, 0), (0, 120), (120, 120), (240, 120), (360, 120), (0, 240), (120, 240), (240, 240), (360, 240), (0, 360), (120, 360), (240, 360)]
nombre = 1


# Définition du texte de victoire
victoire = FONT.render("Victoire", 1, (255, 255, 255))


# Définition de la variable d'histoire
histoire = 0