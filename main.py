from classes import Labyrinthe, MacGyver
import pygame

level1 = Labyrinthe("carte_1.txt")
MG = MacGyver(level1)

"""
Création de l'interface graphique avec pygame



pygame.init()
fenetre = pygame.display.set_mode((640, 480))

pygame.display.flip()

while level1.continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level1.continuer = False
            pygame.quit()
"""

while level1.continuer:

    level1.display_laby()
    direction = input()
    if direction == "z":  # haut
        MG.move(direction)
    elif direction == "s":  # bas
        MG.move(direction)
    elif direction == "q":  # gauche
        MG.move(direction)
    elif direction == "d":  # droite
        MG.move(direction)
