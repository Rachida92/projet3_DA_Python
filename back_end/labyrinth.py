import random

"""
Module to create labyrinth complete
with objects to get
"""


class Labyrinth:
    """
    Initialization :
    - Creating labyrinth
    from textfile and fill it in "map" list.
    - "coordinates" list gets all the position tuples existing.
    - "empty_space" list gets all the position tuples
    corresponding with empty spaces.
    - "random_location" list gets 3 random positions from "empty_space"
    - "objects" list contains the 3 objects MG needs to get to win.
    - "running" is used to stop the loop game.
    """

    def __init__(self, textfile):
        self.running = True
        self.map = []
        self.coordinates = []
        self.objects = ["T", "A", "E"]
        self.random_location = []
        self.empty_space = []

        # Fill all the positions tuple possible in the list "coordinates"
        for x in range(15):
            for y in range(15):
                self.coordinates.append((x, y))

        # Open, read the textfile and fill it in the list "map"
        with open(textfile, "r") as f:
            for map_file in f.readlines():

                lines = []
                for item in map_file:
                    if item != "\n":
                        lines.append(item)
                self.map.append(lines)

            # Fill all the positions tuple containing empty space
            for (x, y) in self.coordinates:
                if self.map[x][y] == " ":
                    self.empty_space.append((x, y))

            # Function below called to place 3 random objects
            self.place_object()

    def place_object(self):
        """
        Function to place 3 objects to random places.
        It fill random_location from 3 random tuples from empty_space
        and place 3 objects on the random tuples.
        """

        # Loop to choose randomly 3 tuples from empty_space
        i = 3
        while i > 0:
            self.random_location.append(random.choice(self.empty_space))
            i -= 1

        # Loop to place the 3 objects on tuples chosen above.
        i = 3
        while i > 0:
            for (x, y) in self.random_location:
                self.map[x][y] = self.objects[i - 1]
                i -= 1
