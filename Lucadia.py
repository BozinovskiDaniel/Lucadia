import pygame
pygame.init()

GAMESIZE  = (1280, 720)

win = pygame.display.set_mode(GAMESIZE)
pygame.display.set_caption("Lucadia")

charSize = (150, 100)

walkRight = [pygame.image.load('Character/adventurer-run-00.png'), pygame.image.load('Character/adventurer-run-01.png'), pygame.image.load('Character/adventurer-run-02.png'), pygame.image.load('Character/adventurer-run-03.png'), pygame.image.load('Character/adventurer-run-04.png'), pygame.image.load('Character/adventurer-run-05.png')]
walkLeft = [pygame.image.load('Character/adventurer-run-00.png'), pygame.image.load('Character/adventurer-run-01.png'), pygame.image.load('Character/adventurer-run-02.png'), pygame.image.load('Character/adventurer-run-03.png'), pygame.image.load('Character/adventurer-run-04.png'), pygame.image.load('Character/adventurer-run-05.png')]
char = pygame.image.load('Character/adventurer-idle-2-00.png')
char = pygame.transform.scale(char, charSize)

for i in range(len(walkRight)):
    walkRight[i] = pygame.transform.scale(walkRight[i].convert_alpha(), charSize)
    walkLeft[i] = pygame.transform.flip(pygame.transform.scale(walkLeft[i].convert_alpha(), charSize), True, False)



scroll = [0, 0]
bg = [pygame.image.load('Background/country-platform-back.png').convert_alpha(), pygame.image.load('Background/country-platform-forest.png').convert_alpha(), pygame.image.load('Background/country-platform-tiles-example.png').convert_alpha()]

bg2 = [pygame.image.load('Background/country-platform-back.png').convert_alpha(), pygame.image.load('Background/country-platform-forest.png').convert_alpha(), pygame.image.load('Background/country-platform-tiles-example-1.png').convert_alpha()]

for i in range(len(bg)):
    bg[i] = pygame.transform.scale(bg[i], GAMESIZE)

for i in range(len(bg2)):
    bg2[i] = pygame.transform.scale(bg2[i], GAMESIZE)


clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.x += scroll[0]
        self.y += scroll[1]
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x - scroll[0],self.y - scroll[1]))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x - scroll[0],self.y - scroll[1]))
            self.walkCount +=1
        else:
            win.blit(char, (self.x - scroll[0],self.y - scroll[1]))



def redrawGameWindow():
    
    for layers in bg:
        win.blit(layers, (0 - scroll[0], 0 - scroll[1]))
        win.blit(layers, (-1280 - scroll[0], 0 - scroll[1]))

    for layers2 in bg2:
        win.blit(layers2, (1280 - scroll[0], 0 - scroll[1]))



    scroll[0] += (man.getx() - scroll[0] - 550)
    man.draw(win)
    
    pygame.display.update()


#mainloop
man = player(100, 520, 64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT]:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if keys[pygame.K_LSHIFT]:
        man.x += man.vel
        man.right = True
        man.left = False

    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    
    redrawGameWindow()

pygame.quit()