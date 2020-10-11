from modules.labyrinthe import Labyrinth
from modules.macgyver import MacGyver
from modules.variables import *
import pygame
from pygame.locals import *

level1 = Labyrinth("carte_1.txt")
MG = MacGyver(level1)

pygame.init()
while level1.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level1.running = False
            pygame.quit()


    screen = pygame.display.set_mode((screen_size, screen_size))

    mur = pygame.image.load("mur.png").convert_alpha()
    mur_petit = pygame.transform.scale(mur, (sprite_size, sprite_size))
    macgyver = pygame.image.load("macgyver_ressources/MacGyver.png").convert_alpha()
    macgyver_petit = pygame.transform.scale(macgyver, (sprite_size, sprite_size))
    guardian = pygame.image.load("macgyver_ressources/Gardien.png").convert_alpha()
    guardian_petit = pygame.transform.scale(guardian, (sprite_size, sprite_size))

    for (x, y) in level1.coor:
        if level1.map[x][y] == 'm':
            screen.blit(mur_petit, ((y * sprite_size, x * sprite_size), (sprite_size, sprite_size)))
        elif level1.map[x][y] == 'M':
            screen.blit(macgyver_petit, ((y * sprite_size, x * sprite_size), (sprite_size, sprite_size)))
        elif level1.map[x][y] == 'a':
            screen.blit(guardian_petit, ((y * sprite_size, x * sprite_size), (sprite_size, sprite_size)))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                MG.move('droite')
            elif event.key == K_LEFT:
                MG.move('gauche')
            elif event.key == K_UP:
                MG.move('haut')
            elif event.key == K_DOWN:
                MG.move('bas')

