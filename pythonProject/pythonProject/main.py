import pygame
from player import *
from projectile import *
from enemies import *

pygame.init()

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("NIMI")
clock = pygame.time.Clock()
floor = pygame.image.load("pildid/floor1.png")
floor = pygame.transform.scale(floor, (1280, 380))
background = pygame.image.load('pildid\scene.jpg')




background = pygame.image.load('pildid\scene.jpg')
background = pygame.transform.scale(background, (screenWidth, screenHeight))

# siin kõik ekraanile kuvatav


def GameWindow():
    screen.blit(background, (0, 0))
    screen.blit(floor, (0, 360))
    for bullet in bullets:
        bullet.draw(screen)

    character.draw(screen)
    enemy.draw(screen)
    pygame.display.update()


character = Player(500, 500, 130, 150)
bullets = []
enemy = Enemy(400, 500, 130, 150, 850)

# peaprogramm

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if screenWidth > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        if character.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 16:
            bullets.append(Projectile(round(character.x + character.width // 2), round(character.y + character.height // 2), 8, (0, 0, 0), facing))
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
        if keys[pygame.K_UP]:
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
