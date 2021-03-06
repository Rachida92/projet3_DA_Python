"""
Module to create and manage moves of main character
"""


class MacGyver:
    """
    This class create MacGyver.
    - Initialization with the initial position of MG, map and list of objects
    that MG should to get to win.
    - Direction dictionary to stock all the moves possible.
    - Two variables (syringe and lose) to manage if player win or lose.
    """

    def __init__(self, labyrinth):

        self.direction = {
            'up': {'x': -1, 'y': 0},
            'down': {'x': 1, 'y': 0},
            'left': {'x': 0, 'y': -1},
            'right': {'x': 0, 'y': 1}
        }
        self.x = 0
        self.y = 0
        self.labyrinth = labyrinth
        self.labyrinth.map[self.x][self.y] = "M"
        self.mg_objects = []
        self.syringe = False
        self.lose = False

    """
    Function to check what is the next position chosen
    and what is the action according with
    """

    def check_collision(self, x, y):

        if x < 0 or y < 0 or x > 14 or y > 14:
            return False

        # Lose
        if self.labyrinth.map[x][y] == "a":
            if len(self.mg_objects) < 3:
                self.labyrinth.running = False
                self.lose = True
            # Win
            else:
                self.labyrinth.running = False
                self.syringe = True
                return True

        # Case defining action when MG is in the same location as an object
        if self.labyrinth.map[x][y] in self.labyrinth.objects:
            self.mg_objects.append(self.labyrinth.map[x][y])
            return True

        # Case to forbid to MG to go on wall locations
        if self.labyrinth.map[x][y] != "m":
            return True

    """
    Function to moving MG
    Check if the move is possible by :
    - check_collision function
    - direction
    Replace previous position of MG by empty space
    """

    def move(self, movement):

        if movement in self.direction and self.check_collision(
                self.x + self.direction[movement]['x'],
                self.y + self.direction[movement]['y']
        ):
            self.x = self.x + self.direction[movement]['x']
            self.y = self.y + self.direction[movement]['y']
            self.labyrinth.map[self.x][self.y] = "M"
            self.labyrinth.map[
                self.x - self.direction[movement]['x']
            ][self.y - self.direction[movement]['y']] = " "
