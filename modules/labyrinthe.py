from random import randint


class Labyrinth:

    def __init__(self, textfile):
        self.running = True
        self.map = []
        self.coor = []
        self.objects = ["T", "A", "E"]

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

    #        self.place_object()

    #    def display_map(self):

    #        for line in self.map:
    #            mapline = ""
    #            for item in line:
    #                mapline += item
    #            print(mapline)

    # update place_object pour placer dans une liste de tuple vide que d'essayer de placer au pif
    def place_object(self):

        i = 3

        while i > 0:
            a = randint(0, 14)
            b = randint(0, 14)

            if self.map[a][b] == " ":
                self.map[a][b] = self.objects[i - 1]
                i -= 1
