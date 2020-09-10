import random

#definition de la classe Personnage pour créer MG et le méchant
class MacGyver:
    def __init__(self, labyrinthe):
        self.x = 0
        self.y = 0
        
        
        self.labyrinthe = labyrinthe
        self.labyrinthe.laby[self.y][self.x] = "M"
        self.objets = []

    def check_collision(self,a,b):

        if self.labyrinthe.laby[a][b] == "a":
            self.labyrinthe.continuer = 0
            print("vous avez gagné")
            return True

        if self.labyrinthe.laby[a][b] != "m":
            return True
        
    


    def move(self,direction):  
                
        
        

        if direction == "s":
            if self.check_collision(self.y+1,self.x):
                self.y += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y-1][self.x] = " "

            #voir pour remplacer previous y par un   ici.
 
        elif direction == "z":            
            if self.check_collision(self.y-1,self.x):
                self.y -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y+1][self.x] = " "
        
        elif direction == "q":            
            if self.check_collision(self.y,self.x-1):
                self.x -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x+1] = " "
        
        elif direction == "d": 
                      
            if self.check_collision(self.y,self.x+1):
                self.x += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x-1] = " "

    
        
        




class Labyrinthe:
    def __init__(self, textfile):
        self.continuer = 1
        self.laby = []
        self.a = 0
        

        

        with open(textfile, "r") as f:
            for contenu in f.readlines():
                            
                lines = []
                for element in contenu:
                    if element != "\n":
                        lines.append(element)                        
                self.laby.append(lines)
        # appeler place_object ici 
        
        #self.place_object(self.a)
    

    def display_laby(self):
        for line in self.laby:
            labyline = ""
            for element in line:
                labyline += element
            print(labyline)

#début d'essai de création de la méthode
    #def place_object(self, objet1):
        
        #if self.labyrinthe.laby[randint(0,15)][randint(0,15)] == " ":
        
                
           

            




