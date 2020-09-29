from random import randint
import pygame

class Labyrinthe:

    def __init__(self, textfile):
        self.continuer = True
        self.laby = []
        self.objets = ["T", "A", "E"]
        self.taille_pixels = 30
        

        with open(textfile, "r") as f:
            for contenu in f.readlines():

                lines = []
                for element in contenu:
                    if element != "\n":
                        lines.append(element)
                self.laby.append(lines)

        self.place_object()

        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))

        

    def display_laby(self):
        for k,line in enumerate(self.laby):
            for h,element in enumerate(line):
                if element == 'm':
                    self.screen.blit('mur.png',(h*self.taille_pixels,k*self.taille_pixels))
                #elif element == 'a':



    def place_object(self):

        i = 3

        while i > 0:
            a = randint(0, 14)
            b = randint(0, 14)

            if self.laby[a][b] == " ":
                self.laby[a][b] = self.objets[i - 1]
                i -= 1


"""
        #premier essai ajout d'une image de mur
        mur = pygame.image.load("mur.png").convert()
        for i in self.laby:
            if i == 'm':
                fenetre.blit(mur, (0,0))
"""