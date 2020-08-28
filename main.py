from classes import Labyrinthe, MacGyver

level1 = Labyrinthe("carte_1.txt")
MG = MacGyver(level1)

"""
position supposée
x = nombre d'éléments
y = nombre de lignes
"""

continuer = 1
while continuer:
    #boucle de jeu
    level1.display_laby()
    direction = input("Dans quelle direction voulez-vous aller : ")
    if direction == "z": #haut
        print("Vous voulez aller en haut")
    elif direction == "s": #bas
        MG.move(direction)
    elif direction == "q": #gauche
        print("Vous voulez aller en gauche")
    elif direction == "d": #droite
        print("Vous voulez aller en droite")


