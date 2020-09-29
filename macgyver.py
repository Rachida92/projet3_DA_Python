class MacGyver:
    def __init__(self, labyrinthe):
        self.x = 0
        self.y = 0
        self.labyrinthe = labyrinthe
        self.labyrinthe.laby[self.y][self.x] = "M"
        self.MGobjets = []
        self.seringue = False

    def check_collision(self, a, b):
        if self.labyrinthe.laby[a][b] == "a":
            if len(self.MGobjets) < 3:
                self.labyrinthe.continuer = False
                print("Vous avez perdu")
            else:
                self.labyrinthe.continuer = False
                self.seringue = True
                print("vous avez gagné")
                return True

        if self.labyrinthe.laby[a][b] in self.labyrinthe.objets:
            self.MGobjets.append(self.labyrinthe.laby[a][b])
            return True

        if self.labyrinthe.laby[a][b] != "m":
            return True

    def move(self, direction):

        if direction == "s":
            if self.check_collision(self.y + 1, self.x):
                self.y += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y - 1][self.x] = " "

            # voir pour remplacer previous y par un   ici.

        elif direction == "z":
            if self.check_collision(self.y - 1, self.x):
                self.y -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y + 1][self.x] = " "

        elif direction == "q":
            if self.check_collision(self.y, self.x - 1):
                self.x -= 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x + 1] = " "

        elif direction == "d":
            if self.check_collision(self.y, self.x + 1):
                self.x += 1
                self.labyrinthe.laby[self.y][self.x] = "M"
                self.labyrinthe.laby[self.y][self.x - 1] = " "