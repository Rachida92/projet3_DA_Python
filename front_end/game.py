from back_end import Labyrinth
from back_end import MacGyver
from back_end import sprite_size as ss, screen_size
import pygame
from pygame.locals import KEYDOWN, K_UP, K_LEFT, K_DOWN, K_RIGHT


class Game():

    def __init__(self):
        # Loading map and MacGyver
        level1 = Labyrinth("front_end/maps/map_1.txt")
        MG = MacGyver(level1)

        # Pygame initialization and start loop game
        pygame.init()
        while level1.running:

            # Game window created and size defined
            screen = pygame.display.set_mode((screen_size, screen_size))
            pygame.display.set_caption("MacGyver Escape")

            # Loading and resizing all the images used
            # First, loading floor and walls images
            mur = pygame.image.load("front_end/macgyver_ressources/mur.png").convert()
            mur_s = pygame.transform.scale(mur, (ss, ss))
            sol = pygame.image.load("front_end/macgyver_ressources/sol.png").convert()
            sol_s = pygame.transform.scale(sol, (ss, ss))

            # Then, loading characters images and objects images
            macgyver = pygame.image.load("front_end/macgyver_ressources/MacGyver.png").convert()
            macgyver_s = pygame.transform.scale(macgyver, (ss, ss))
            guardian = pygame.image.load("front_end/macgyver_ressources/Gardien.png").convert()
            guardian_s = pygame.transform.scale(guardian, (ss, ss))
            ether = pygame.image.load("front_end/macgyver_ressources/ether.png").convert()
            ether_s = pygame.transform.scale(ether, (ss, ss))
            tube = pygame.image.load("front_end/macgyver_ressources/tube.png").convert()
            tube_s = pygame.transform.scale(tube, (ss, ss))
            needle = pygame.image.load("front_end/macgyver_ressources/aiguille.png").convert()
            needle_s = pygame.transform.scale(needle, (ss, ss))

            images = {
                'm': mur_s,
                'M': macgyver_s,
                'a': guardian_s,
                'T': tube_s,
                'A': needle_s,
                'E': ether_s,
                ' ': sol_s
            }
            # Applying all the images loaded to the correct location

            for (x, y) in level1.coordinates:
                finalSizeX = x * ss
                finalSizeY = y * ss
                if level1.map[x][y] in images.keys():
                    screen.blit(images[level1.map[x][y]],
                                ((finalSizeY, finalSizeX),
                                 (ss, ss)))

            # Game window refresh with all the images
            pygame.display.flip()

            # Events configuration (key pressed and clic to close the game window)

            # Close the window if user clic to close window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    level1.running = False

                # Direction of MacGyver configurations
                events_direction = {
                    K_RIGHT: 'droite',
                    K_LEFT: 'gauche',
                    K_DOWN: 'bas',
                    K_UP: 'haut'
                }
                if event.type == KEYDOWN:
                    if event.key in events_direction.keys():
                        MG.move(events_direction[event.key])

        pygame.quit()
