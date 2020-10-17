import random


# Labyrinth class to generate map with 3 random objects placed on.
class Labyrinth:

    # Initialization with boolean for game loop, all the lists needed for the map
    def __init__(self, textfile):
        self.running = True
        self.map = []
        self.coor = []
        self.objects = ["T", "A", "E"]
        self.random_location = []
        self.empty_space = []

        # Fill all the positions tuple possible in the list "coor"
        for x in range(15):
            for y in range(15):
                self.coor.append((x, y))

        # Open, read the textfile and fill it in the list "map"
        with open(textfile, "r") as f:
            for mapfile in f.readlines():

                lines = []
                for item in mapfile:
                    if item != "\n":
                        lines.append(item)
                self.map.append(lines)

            # Fill all the positions tuple containing empty space
            for (x, y) in self.coor:
                if self.map[x][y] == " ":
                    self.empty_space.append((x, y))

            # Call place_object function to place the 3 objects to random places
            self.place_object()

    # Function to place 3 objects to random places
    def place_object(self):

        # Loop to choose 3 randoms tuples in the list "empty_space" and add them to the list "random_location"
        i = 3
        while i > 0:
            self.random_location.append(random.choice(self.empty_space))
            i -= 1

        # Loop to place the 3 objects from the list "objects"
        i = 3
        while i > 0:
            for (x, y) in self.random_location:
                self.map[x][y] = self.objects[i - 1]
                i -= 1
