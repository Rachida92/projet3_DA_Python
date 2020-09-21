from classes import Labyrinthe, MacGyver
import pygame

level1 = Labyrinthe("carte_1.txt")
MG = MacGyver(level1)

while level1.continuer:
    #boucle de jeu
    level1.display_laby()
    direction = input()
    if direction == "z": #haut
        MG.move(direction)
    elif direction == "s": #bas
        MG.move(direction)
    elif direction == "q": #gauche
        MG.move(direction)
    elif direction == "d": #droite
        MG.move(direction)




