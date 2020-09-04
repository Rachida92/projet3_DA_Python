from classes import Labyrinthe, MacGyver

level1 = Labyrinthe("carte_1.txt")
MG = MacGyver(level1)


continuer = 1
while continuer:
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

