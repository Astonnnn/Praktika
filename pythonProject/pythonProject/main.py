import pygame
from player import *

pygame.init()

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("NIMI")
clock = pygame.time.Clock()
floor = pygame.image.load("pildid/floor1.png")
floor = pygame.transform.scale(floor, (1280, 380))
background = pygame.image.load('pildid\scene.jpg')


character = Player(500, 500, 130, 150)

background = pygame.image.load('pildid\scene.jpg')
background = pygame.transform.scale(background, (screenWidth, screenHeight))

# siin kõik ekraanile kuvatav

def GameWindow():
    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 360))
    character.draw(screen)
    pygame.display.update()


# peaprogramm

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
        character.idleCount = 0
        character.standing = False
    elif keys[pygame.K_RIGHT] and character.x < screenWidth - character.width:
        character.x += character.vel
        character.right = True
        character.left = False
        character.idleCount = 0
        character.standing = False
    else:
        character.walkCount = 0
        character.standing = True
    if not character.isJump:
        if keys[pygame.K_SPACE]:
            character.isJump = True
            character.walkCount = 0
            character.idleCount = 0
    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.y -= (character.jumpCount ** 2) * 0.6 * neg
            character.jumpCount -= 1
        else:
            character.isJump = False
            character.jumpCount = 10

    GameWindow()
    clock.tick(48)
