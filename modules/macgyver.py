class MacGyver:

    def __init__(self, labyrinth):
        self.x = 0
        self.y = 0
        self.labyrinth = labyrinth
        self.labyrinth.map[self.x][self.y] = "M"
        self.MGobjects = []
        self.seringue = False

    def check_collision(self, x, y):
        if self.labyrinth.map[x][y] == "a":
            if len(self.MGobjects) < 3:
                self.labyrinth.running = False
                print("Vous avez perdu")


            else:
                self.labyrinth.running = False
                self.seringue = True
                print("vous avez gagné")

                return True


        if self.labyrinth.map[x][y] in self.labyrinth.objects:
            self.MGobjects.append(self.labyrinth.map[x][y])
            return True

        if self.labyrinth.map[x][y] != "m":
            return True

    def move(self, direction):

        if direction == 'droite':
            if self.check_collision(self.x, self.y + 1):
                self.y += 1
                self.labyrinth.map[self.x][self.y] = "M"
                self.labyrinth.map[self.x][self.y - 1] = " "

        elif direction == 'gauche':
            if self.check_collision(self.x, self.y - 1):
                self.y -= 1
                self.labyrinth.map[self.x][self.y] = "M"
                self.labyrinth.map[self.x][self.y + 1] = " "

        elif direction == 'haut':
            if self.check_collision(self.x - 1, self.y):
                self.x -= 1
                self.labyrinth.map[self.x][self.y] = "M"
                self.labyrinth.map[self.x + 1][self.y] = " "

        elif direction == 'bas':
            if self.check_collision(self.x + 1, self.y):
                self.x += 1
                self.labyrinth.map[self.x][self.y] = "M"
                self.labyrinth.map[self.x - 1][self.y] = " "
