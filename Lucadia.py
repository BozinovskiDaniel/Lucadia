import pygame, sys

from pygame.locals import *

timer = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Lucadia')

WINDOW_SIZE = (500, 500)

player = pygame.image.load('Character/adventurer-run-00.png')
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

move_right = False
move_left = False

while True:

    screen.blit(player, (50, 50))
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False

    pygame.display.update()
    timer.tick(60)