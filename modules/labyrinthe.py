import random


class Labyrinth:

    def __init__(self, textfile):
        self.running = True
        self.map = []
        self.coor = []
        self.objects = ["T", "A", "E"]
        self.object_place = []
        self.empty_space = []

        for x in range(15):
            for y in range(15):
                self.coor.append((x, y))

        with open(textfile, "r") as f:
            for mapfile in f.readlines():

                lines = []
                for item in mapfile:
                    if item != "\n":
                        lines.append(item)
                self.map.append(lines)

            for (x, y) in self.coor:
                if self.map[x][y] == " ":
                    self.empty_space.append((x, y))

            i = 3
            while i > 0:
                self.object_place.append(random.choice(self.empty_space))
                i -= 1

            self.place_object()

    def place_object(self):

        i = 3
        while i > 0:

            for (x, y) in self.object_place:
                self.map[x][y] = self.objects[i - 1]
                i -= 1
