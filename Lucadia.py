import pygame
pygame.init()

screenWidth = 750
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Lucadia")

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

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
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
    

class projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing


def redrawGameWindow():
    win.blit(bg, (0, 0))
    daniel.draw(win)
    pygame.display.update()

# Main loop
daniel = player(300, 410, 64, 64)
run = True

while run:
    clock.tick(27)

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