import pygame

pygame.init()

screenWidth = 1280
screenHeight = 720


screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("NIMI")



x = 500
y = 500
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth-width:
        x += vel
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (x,  y, width, height))
    pygame.display.update()