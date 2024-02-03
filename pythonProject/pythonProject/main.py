import pygame
import player

pygame.init()

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("NIMI")
clock = pygame.time.Clock()
floor = pygame.image.load("pildid/floor1.png")
floor = pygame.transform.scale(floor, (1280, 380))
background = pygame.image.load('pildid\scene.jpg')

walkRight = []
walkLeft = []
for i in range(1, 17):
    walkRight += [pygame.image.load('pildid\Run\cuphead_run_' + str(i) + '.png')]
for i in range(1, 17):
    walkLeft += [pygame.transform.flip(pygame.image.load('pildid\Run\cuphead_run_' + str(i) + '.png'), True, False)]

background = pygame.image.load('pildid\scene.jpg')
background = pygame.transform.scale(background, (screenWidth, screenHeight))


idle = []
for i in range(1, 6):
    idle += [pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png')]
for i in range(4, 0, -1):
    idle += [pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png')]

print(idle)


x = 500
y = 500
width = 130
height = 150
vel = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
idleCount = 0



#siin kõik ekraanile kuvatav

def GameWindow():
    global walkCount
    global idleCount
    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 360))

    if walkCount + 1 >= 48:
        walkCount = 0

    if idleCount + 1 >= 27:
        idleCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(idle[idleCount//3], (x,y))
        idleCount += 1
    pygame.display.update()


#peaprogramm

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        idleCount = 0
    elif keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
        right = True
        left = False
        idleCount = 0
    else:
        right = False
        left = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            idleCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.6 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    GameWindow()
    clock.tick(48)
