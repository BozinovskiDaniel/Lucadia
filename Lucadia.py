import pygame
import numpy as np
pygame.init()

screenWidth = 928
screenHeight = 793
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Lucadia")

walkRight = [pygame.image.load('Game/adventurer-run-00.png').convert_alpha(), pygame.image.load('Game/adventurer-run-01.png').convert_alpha(), pygame.image.load('Game/adventurer-run-02.png').convert_alpha(), pygame.image.load('Game/adventurer-run-03.png').convert_alpha(), pygame.image.load('Game/adventurer-run-04.png').convert_alpha(), pygame.image.load('Game/adventurer-run-05.png').convert_alpha()]
walkLeft = [pygame.image.load('Game/adventurer-run-00.png').convert_alpha(), pygame.image.load('Game/adventurer-run-01.png').convert_alpha(), pygame.image.load('Game/adventurer-run-02.png').convert_alpha(), pygame.image.load('Game/adventurer-run-03.png').convert_alpha(), pygame.image.load('Game/adventurer-run-04.png').convert_alpha(), pygame.image.load('Game/adventurer-run-05.png').convert_alpha()]
bg = [pygame.image.load('Layers/Layer_0000_9.png').convert_alpha(), pygame.image.load('Layers/Layer_0001_8.png').convert_alpha(), pygame.image.load('Layers/Layer_0002_7.png').convert_alpha(), pygame.image.load('Layers/Layer_0003_6.png').convert_alpha(), pygame.image.load('Layers/Layer_0004_Lights.png').convert_alpha(), pygame.image.load('Layers/Layer_0005_5.png').convert_alpha(), pygame.image.load('Layers/Layer_0006_4.png').convert_alpha(), pygame.image.load('Layers/Layer_0007_Lights.png').convert_alpha(), pygame.image.load('Layers/Layer_0008_3.png').convert_alpha(), pygame.image.load('Layers/Layer_0009_2.png').convert_alpha(), pygame.image.load('Layers/Layer_0010_1.png').convert_alpha()]

char = pygame.image.load('Game/adventurer-idle-00.png').convert_alpha()

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
    

def redrawGameWindow():
    for layers in bg[::-1]:
        win.blit(layers, (0, 0))

    daniel.draw(win)
    pygame.display.update()
 
# Main loop
daniel = player(screenWidth/2, 690, 64 , 64)
run = True

while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and daniel.x > daniel.vel:
        daniel.x -= daniel.vel
        daniel.right = False
        daniel.left = True
    
    elif keys[pygame.K_RIGHT] and daniel.x < screenWidth - daniel.width - daniel.vel:
        daniel.x += daniel.vel
        daniel.right = True
        daniel.left = False

    else:
        daniel.right = False
        daniel.left = False
        daniel.walkCount = 0

    if not daniel.isJump:
        if keys[pygame.K_SPACE]:
            daniel.isJump = True
            daniel.right = False
            daniel.left = False
            daniel.walkCount = 0
    else:
        if daniel.jumpCount >= -10:
            neg = 1
            if daniel.jumpCount < 0:
                neg = -1

            daniel.y -= (daniel.jumpCount ** 2) * 0.25 * neg
            daniel.jumpCount -= 1
        else:
            daniel.isJump = False
            daniel.jumpCount = 10

    redrawGameWindow()

pygame.quit()