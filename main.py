# coding=utf-8
# Imports des sprites et des variables
from sprites import *
from variables import *


for i in range(randint(50, 100)):
    b = pieces[randint(0, 14)]
    b.deplacement()

# Boucle de jeu
while not arret_jeu :
    


    # Recuperation des evenements
    for event in pygame.event.get() :

        # Evenements du clavier
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE : # Touche echap = fermeture de la fenêtre
                arret_jeu = True

            if event.key == pygame.K_f: # Touche F = aide au debuggage, resout automatiquement le puzzle
                indic = 0
                for i in all_sprites:
                    i.x = coordonnees2[indic][0]
                    i.y = coordonnees2[indic][1]
                    indic += 1

        # Evenements de la souris, permet d'appeler la methode deplacement() de l'instance de la classe Piece() qui a ete cliquee
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for piece in all_sprites:
                if piece.x <= pos[0] < piece.x + 120 and piece.y <= pos[1] < piece.y + 120:
                    piece.deplacement()
                    break

        # Fermeture de la fenêtre quand la croix est cliquee
        if event.type == pygame.QUIT:
            sys.exit()

    # Definition des variables liees a la condition de victoire
    x = 0
    y = 0

    # Condition de victoire
    for i in all_sprites:
        if i.x == x and i.y == y:
            if i.x == 240 and i.y == 360:
                print("Victoire")
                arret_jeu = True
                sys.exit()
            elif x < 360: 
                x += 120
            else:
                x = 0
                y += 120
        else:
            break


    # Affichage de la grille du puzzle
    ecran.fill(blanc)
    pygame.draw.line(ecran, noir, (480, 0), (480, 480))
    pygame.draw.line(ecran, noir, (480, 480), (0, 480))
    pygame.draw.line(ecran, noir, (120, 0), (120, 480))
    pygame.draw.line(ecran, noir, (240, 0), (240, 480))
    pygame.draw.line(ecran, noir, (360, 0), (360, 480))
    pygame.draw.line(ecran, noir, (0, 120), (480, 120))
    pygame.draw.line(ecran, noir, (0, 240), (480, 240))
    pygame.draw.line(ecran, noir, (0, 360), (480, 360))


    # Mise a jour des objets et de l'ecran
    all_sprites.update()
    pygame.display.update()

    #à garder