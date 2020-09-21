from random import randint
import pygame

class MacGyver:
    def __init__(self, labyrinthe):
        self.x = 0
        self.y = 0
        self.labyrinthe = labyrinthe
        self.labyrinthe.laby[self.y][self.x] = "M"
        self.MGobjets = []

    def check_collision(self,a,b):
        if self.labyrinthe.laby[a][b] == "a":
            if len(self.MGobjets) < 3:
                self.labyrinthe.continuer = 0
                print("Vous avez perdu")
            else:
                self.labyrinthe.continuer = 0
                print("vous avez gagné")
                return True
        
        if self.labyrinthe.laby[a][b] in self.labyrinthe.objets:
            self.MGobjets.append(self.labyrinthe.laby[a][b])
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
        self.objets = ["T","A","E"]
        
        with open(textfile, "r") as f:
            for contenu in f.readlines():
                            
                lines = []
                for element in contenu:
                    if element != "\n":
                        lines.append(element)                        
                self.laby.append(lines)
        
        
        self.place_object()
    
    def display_laby(self):
        for line in self.laby:
            labyline = ""
            for element in line:
                labyline += element
            print(labyline)
 
    def place_object(self):
              
        i = 3
        
        while i > 0:
            a = randint(0,14)
            b = randint(0,14)
            
            if self.laby[a][b] == " ":
                self.laby[a][b] = self.objets[i-1]
                i -= 1


        
           

            




