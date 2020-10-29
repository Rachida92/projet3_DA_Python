from pygame import font, display, time
import pygame as pg
from pygame.locals import KEYDOWN, K_UP, K_LEFT, K_DOWN, K_RIGHT

from back_end import Labyrinth
from back_end import MacGyver
from back_end import sprite_size as ss, screen_size

"""
Module to build graphics with pygame
"""


class Game:
    """
    Class to manage graphics with pygame.
    - Load map with characters and objects on,
    images and end screen.
    - Loop game managed here.
    """

    def __init__(self):
        # Loading map and MacGyver
        level = Labyrinth("front_end/maps/map_1.txt")
        MG = MacGyver(level)

        # Pygame initialization and start loop game
        pg.init()
        while level.running:

            # Game window created and size defined
            screen = pg.display.set_mode((screen_size, screen_size))
            pg.display.set_caption("MacGyver Escape")

            # Loading and resizing all the images used
            # First, loading floor and walls images
            mur = pg.image.load("front_end/MG_img/mur.png").convert()
            mur_s = pg.transform.scale(mur, (ss, ss))
            sol = pg.image.load("front_end/MG_img/sol.png").convert()
            sol_s = pg.transform.scale(sol, (ss, ss))

            # Then, loading characters images and objects images
            macgyver = pg.image.load("front_end/MG_img/MacGyver.png").convert()
            macgyver_s = pg.transform.scale(macgyver, (ss, ss))
            guardian = pg.image.load("front_end/MG_img/Gardien.png").convert()
            guardian_s = pg.transform.scale(guardian, (ss, ss))
            ether = pg.image.load("front_end/MG_img/ether.png").convert()
            ether_s = pg.transform.scale(ether, (ss, ss))
            tube = pg.image.load("front_end/MG_img/tube.png").convert()
            tube_s = pg.transform.scale(tube, (ss, ss))
            needle = pg.image.load("front_end/MG_img/aiguille.png").convert()
            needle_s = pg.transform.scale(needle, (ss, ss))

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

            for (x, y) in level.coordinates:
                finalSizeX = x * ss
                finalSizeY = y * ss
                if level.map[x][y] in images.keys():
                    screen.blit(images[level.map[x][y]],
                                ((finalSizeY, finalSizeX),
                                 (ss, ss)))

            # Game window refresh with all the images
            pg.display.flip()

            # Events configuration

            # Close the window if user clic to close window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    level.running = False

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
            # End screens
            # Win screen
            if MG.seringue:
                font.init()
                my_font = font.Font(font.get_default_font(), 20)
                scr = display.set_mode((screen_size, screen_size))
                scr.blit(my_font.render(
                    "Vous avez gagné !",
                    1,
                    (255, 255, 255)),
                    (200, 250)
                )
                display.flip()
                time.delay(500)
                display.flip()
            # Lose screen
            elif MG.lose:
                font.init()
                my_font = font.Font(font.get_default_font(), 20)
                scr = display.set_mode((screen_size, screen_size))
                scr.blit(my_font.render(
                    "Vous avez perdu",
                    1,
                    (255, 255, 255)),
                    (200, 250)
                )
                display.flip()
                time.delay(500)
                display.flip()

        pg.quit()
