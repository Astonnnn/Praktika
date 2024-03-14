import pygame
from player import *
from projectile import *
from enemies import *
from button import *
from random import *

pygame.init()

screenWidth = 1280
screenHeight = 720

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("NIMI")
clock = pygame.time.Clock()

# PILDID

# floor = pygame.image.load("pildid/floor1.png")
# floor = pygame.transform.scale(floor, (1280, 380))

background = pygame.image.load('pildid\Background.jpeg')
menuBackground = pygame.image.load('pildid\menuBackground.png')
taust = pygame.image.load("pildid\Taust.png")
taust = pygame.transform.scale(taust, (950, 720))


def get_font(size):  # tagastab soovitud suuruses
    return pygame.font.Font("pildid/font.ttf", size)


# heli

bulletSound = pygame.mixer.Sound("pildid\soundEffects\Fireball.mp3")
hitSound = ""

music = pygame.mixer.music.load("pildid\soundEffects\BackgroundMusic.mp3")
pygame.mixer.music.play(-1)

# background = pygame.image.load('pildid\scene.jpg')
background = pygame.transform.scale(background, (screenWidth, screenHeight))


def play():
    pygame.display.set_caption("Play")

    # siin kõik ekraanile kuvatav

    def Gamewindow():
        screen.blit(background, (0, 0))
        # screen.blit(floor, (0, 360))
        text = font.render("Health: " + str(character.health), 1, (255, 255, 255))
        screen.blit(text, (1000, 10))

        time_counter = clock.tick()
        for bullet in bullets:
            bullet.draw(screen)

        character.draw(screen)
        for i in enemies:
            i.draw(screen)
        pygame.display.update()

    milliseconds_delay = 3000
    enemy_spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_spawn_event, milliseconds_delay)

    font = pygame.font.SysFont('comicsans', 45, True)
    character = Player(200, 500, 130, 150)
    bullets = []
    enemies = [Enemy(400, 500, 130, 150, 850)]
    shootloop = 0
    number_of_enemies = 3


    # peaprogramm

    isPaused = False
    run = True
    character.right = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    isPaused = not isPaused
            if event.type == enemy_spawn_event and len(enemies) < number_of_enemies:
                randomX = randint(130, 1150)
                if not character.x + (character.width/2) > randomX > character.x - (character.width/2):
                    enemies.append(Enemy(randomX, 500, 130, 150, (randomX + 450)))
                time_counter = 0

        if not isPaused:

            for enemy in enemies:
                    if character.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and character.hitbox[1] + character.hitbox[3] > enemy.hitbox[1]:
                        if character.hitbox[0] + character.hitbox[2] > enemy.hitbox[0] and character.hitbox[0] - character.hitbox[2] < enemy.hitbox[0] + enemy.hitbox[2]:
                            # hitSound.play()
                            character.hit(screen)
                            character.health -= 1


            if character.health == 0:
                main_menu()
                break


            if shootloop > 0:
                shootloop += 1
            if shootloop > 5:  # number muudab kuulide vahe suuremaks
                shootloop = 0

            for bullet in bullets:
                for enemy in enemies:
                    if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                        if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        # hitSound.play()
                            enemy.hit()
                            bullets.pop(bullets.index(bullet))
                    if enemy.health == 0:
                        enemies.pop(enemies.index(enemy))

                if screenWidth > bullet.x > 0:
                    bullet.x += bullet.vel
                if bullet.x > screenWidth:
                    bullets.pop(bullets.index(bullet))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_z] and shootloop == 0:
                bulletSound.play()
                if character.left:
                    facing = -1
                else:
                    facing = 1
                if len(bullets) < 16:
                    bullets.append(Projectile(round(character.x + character.width // 2),
                                              round(character.y + character.height // 2), 8, (0, 0, 0), facing))

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

            Gamewindow()
            clock.tick(48)
            for bullet in bullets:
                bullet.imageCount += 1

        if isPaused:
            screen.blit(taust, (150, 0))
            pause_text = font.render("Paused", True, "black")
            screen.blit(pause_text,
                        ((screenWidth - pause_text.get_width()) // 2, (screenHeight - pause_text.get_height()) // 2))
            pygame.display.flip()


def options():
    pygame.display.set_caption("Options")

    while True:
        optionsMousePosition = pygame.mouse.get_pos()

        screen.blit(menuBackground, (0, 0))
        screen.blit(taust, (150, 0))

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(optionsMousePosition)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(optionsMousePosition):
                    main_menu()
                    break



        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(menuBackground, (0, 0))

        menuMousePosition = pygame.mouse.get_pos()

        menuText = get_font(100).render("MAIN MENU", True, (182, 143, 64))
        menuRect = menuText.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("pildid/nupud/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("pildid/nupud/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("pildid/nupud/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menuText, menuRect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(menuMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(menuMousePosition):
                    play()
                    break
                if OPTIONS_BUTTON.checkForInput(menuMousePosition):
                    options()
                    break
                if QUIT_BUTTON.checkForInput(menuMousePosition):
                    pygame.quit()
                    break


        pygame.display.update()


main_menu()
