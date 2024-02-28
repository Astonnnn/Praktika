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
    text = font.render("Score: " + str(score), 1, (0,0,0))
    screen.blit(text, (1000,10))
    for bullet in bullets:
        bullet.draw(screen)

    character.draw(screen)
    enemy.draw(screen)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 45, True)
character = Player(500, 500, 130, 150)
bullets = []
enemy = Enemy(400, 500, 130, 150, 850)
shootloop = 0
score = 0

# peaprogramm

run = True
while run:

    if shootloop > 0:
        shootloop += 1
    if shootloop > 5:  #number muudab kuulide vahe suuremaks
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if screenWidth > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z] and shootloop == 0:
        if character.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 16:
            bullets.append(Projectile(round(character.x + character.width // 2), round(character.y + character.height // 2), 8, (0, 0, 0), facing))

        shootloop = 1

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
