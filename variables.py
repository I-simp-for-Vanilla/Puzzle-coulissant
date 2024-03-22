# coding=utf-8

# Import des modules
import pygame, sys
from random import randint
pygame.init()


# Definition de la variable de jeu
arret_jeu = False


# Affichage de l'ecran
ecran = pygame.display.set_mode((480, 480))


# Definition du nom de la fenêtre
pygame.display.set_caption("Puzzle coulissant")


# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)


# Font
FONT = pygame.font.Font(None, 24)


# Definition des variables liees au melange des pièces
coordonnees2 = [(0, 0), (120, 0), (240, 0), (360, 0), (0, 120), (120, 120), (240, 120), (360, 120), (0, 240), (120, 240), (240, 240), (360, 240), (0, 360), (120, 360), (240, 360)]
nombre = 1


# Definition du texte de victoire
victoire = FONT.render("Victoire", 1, (255, 255, 255))


# Definition de la variable d'histoire
histoire = 0