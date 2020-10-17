# MacGyver class to create, place on the map and manage moves of the character

class MacGyver:
    """
    This class create MG
    """

    # Initialization with the initial position of MG, map and list of objects.
    def __init__(self, labyrinth):
        self.direction = {
            'haut': {'x': -1, 'y': 0},
            'bas': {'x': 1, 'y': 0},
            'gauche': {'x': 0, 'y': -1},
            'droite': {'x': 0, 'y': 1}
        }
        self.x = 0
        self.y = 0
        self.labyrinth = labyrinth
        self.labyrinth.map[self.x][self.y] = "M"
        self.MGobjects = []
        self.seringue = False

    # Function to check what is the next position chosen and what is the action according with
    def check_collision(self, x, y):
        # Case defining conditions to win or lose when MG is in the same location as guardian
        if self.labyrinth.map[x][y] == "a":
            if len(self.MGobjects) < 3:
                self.labyrinth.running = False
                print("Vous avez perdu")
            else:
                self.labyrinth.running = False
                self.seringue = True
                print("vous avez gagné")
                return True
        # Case defining action when MG is in the same location as an object
        if self.labyrinth.map[x][y] in self.labyrinth.objects:
            self.MGobjects.append(self.labyrinth.map[x][y])
            return True
        # Case to forbid to MG to go on wall locations
        if self.labyrinth.map[x][y] != "m":
            return True

    # Function for moving MG
    def move(self, movement):

        if movement in self.direction:
            if self.check_collision(self.x + self.direction[movement]['x'], self.y + self.direction[movement]['y']):
                self.x = self.x + self.direction[movement]['x']
                self.y = self.y + self.direction[movement]['y']
                self.labyrinth.map[self.x][self.y] = "M"
                self.labyrinth.map[self.x - self.direction[movement]['x']][self.y - self.direction[movement]['y']] = " "
