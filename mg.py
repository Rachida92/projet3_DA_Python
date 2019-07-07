import csv
import numpy as np

file = open(r'C:/Users/rbent/Desktop/git_repository/projet3_DA_Python/structure.csv')

#definition de la classe Personnage pour créer MG et le méchant
class Personnage:
    def __init__(self, name, image, position):
        self.name = name
        self.image = image
        self.position = position

#création de deux instances. MG et le méchant avec des attributs différents
MG = Personnage("Mac Gyver", "none", 0)
mechant = Personnage("Mechant", "none",0)

#print(mechant.name)
#print(mechant.image)
#print(mechant.position)

#création du labyrithe qui ouvre et lit un fichier csv qui affiche les 15 lignes et colonnes du fichier
class Labyrinthe:
    reader = csv.reader(file)
    for row in reader:
        print(row)



#un test avec numpy pour afficher une grille de 0 qui fonctionne
a = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
print(a)
