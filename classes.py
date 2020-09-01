#definition de la classe Personnage pour créer MG et le méchant
class MacGyver:
    def __init__(self, labyrinthe):
        self.x = 0
        self.y = 0
        
        self.position = (self.y,self.x)
        self.labyrinthe = labyrinthe
        self.labyrinthe.laby[self.position[0]][self.position[1]] = "M"

    def move(self,direction):  
        
        if direction == "s":
            
            self.position = (self.y+1,self.x)
            self.labyrinthe.laby[self.position[0]][self.position[1]] = "M"
            
        
        if direction == "z":
            
            self.position = (self.y-1,self.x)
            self.labyrinthe.laby[self.position[0]][self.position[1]] = "M"
        
        if direction == "q":
            
            self.position = (self.y,self.x-1)
            self.labyrinthe.laby[self.position[0]][self.position[1]] = "M"
        
        if direction == "d":
            
            self.position = (self.y,self.x+1)
            self.labyrinthe.laby[self.position[0]][self.position[1]] = "M"
        




#création du labyrithe qui ouvre et lit un fichier csv qui affiche les 15 lignes et colonnes du fichier

class Labyrinthe:
    def __init__(self, textfile):

        self.laby = []

        with open(textfile, "r") as f:
            for contenu in f.readlines():
                            
                lines = []
                for element in contenu:
                    if element != "\n":
                        lines.append(element)                        
                self.laby.append(lines)
        

    def display_laby(self):
        for line in self.laby:
            labyline = ""
            for element in line:
                labyline += element
            print(labyline)

            

            




