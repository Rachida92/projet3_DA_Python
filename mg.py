#definition de la classe Personnage pour créer MG et le méchant
class Personnage:
    def __init__(self, name, image, position):
        self.name = name
        self.image = image
        self.position = position

#création de deux instances. MG et le méchant avec des attributs différents
MG = Personnage("Mac Gyver", "none", 0)
#mechant = Personnage("Mechant", "none",0)

#print(mechant.name)
#print(mechant.image)
#print(mechant.position)

#création du labyrithe qui ouvre et lit un fichier csv qui affiche les 15 lignes et colonnes du fichier

class Labyrinthe:
    def __init__(self, textfile):
        laby = []

        with open(textfile, "r") as f:
            for contenu in f.readlines():
                            
                line = []
                for i in contenu:
                    if i != "\n":
                        line.append(i)
                laby.append(line)

        print(laby)

            




