#definition de la classe Personnage pour créer MG et le méchant
class MacGyver:
    def __init__(self, labyrinthe):
        self.x = 0
        self.y = 0
        
        
        self.labyrinthe = labyrinthe
        self.labyrinthe.laby[self.y][self.x] = "M"

    #def check_collision(self,x,y):
    #    if self.y+1 == "m":                  
        
    #    if self.x+1 == "m":
            
            

            
        # vérifier si le futur x est un mur.


    def move(self,direction):  
                
        
        

        if direction == "s":
            if self.labyrinthe.laby[self.y+1][self.x] != "m":
                self.y += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y-1][self.x] = "0"

            #voir pour remplacer previous y par un 0 ici.
 
        elif direction == "z":            
            if self.labyrinthe.laby[self.y-1][self.x] != "m":
                self.y -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y+1][self.x] = "0"
        
        elif direction == "q":            
            if self.labyrinthe.laby[self.y][self.x-1] != "m":
                self.x -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x+1] = "0"
        
        elif direction == "d": 
                      
            if self.labyrinthe.laby[self.y][self.x+1] != "m":
                self.x += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x-1] = "0"

    
        
        




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

            

            




