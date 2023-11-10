# Imports des sprites et des variables
from sprites import *
from variables import *


for i in range(randint(50, 100)):
    b = pièces[randint(0, 14)]
    b.déplacement()

# Boucle de jeu
while not arret_jeu :
    


    # Récupération des évènements
    for event in pygame.event.get() :

        # Évènements du clavier
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE : # Touche échap = fermeture de la fenêtre
                arret_jeu = True

            if event.key == pygame.K_f: # Touche F = aide au débuggage, résout automatiquement le puzzle
                indic = 0
                for i in all_sprites:
                    i.x = coordonnées2[indic][0]
                    i.y = coordonnées2[indic][1]
                    indic += 1

        # Évènements de la souris, permet d'appeler la méthode déplacement() de l'instance de la classe Pièce() qui a été cliquée
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for pièce in all_sprites:
                if pièce.x <= pos[0] < pièce.x + 120 and pièce.y <= pos[1] < pièce.y + 120:
                    pièce.déplacement()
                    break

        # Fermeture de la fenêtre quand la croix est cliquée
        if event.type == pygame.QUIT:
            sys.exit()

    # Définition des variables liées à la condition de victoire
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


    # Mise à jour des objets et de l'écran
    all_sprites.update()
    pygame.display.update()