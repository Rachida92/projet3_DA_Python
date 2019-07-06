import csv
import numpy as np

class Personnage:
    def __init__(self, name, image, position):
        self.name = name
        self.image = image
        self.position = position


MG = Personnage("Mac Gyver", "none", 0)
mechant = Personnage("Mechant", "none",0)


#print(mechant.name)
#print(mechant.image)
#print(mechant.position)

class Labyrinthe:
    pass

    
a = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])


print(a)