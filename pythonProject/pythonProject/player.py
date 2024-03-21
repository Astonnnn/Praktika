import pygame

walkRight = []
walkLeft = []
for i in range(1, 17):
    walkRight += [pygame.image.load('pildid\Run\cuphead_run_' + str(i) + '.png')]
for i in range(1, 17):
    walkLeft += [pygame.transform.flip(pygame.image.load('pildid\Run\cuphead_run_' + str(i) + '.png'), True, False)]


idleRight = []
for i in range(1, 6):
    idleRight += [pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png')]
for i in range(4, 0, -1):
    idleRight += [pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png')]

idleLeft = []
for i in range(1, 6):
    idleLeft += [pygame.transform.flip(pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png'), True, False)]
for i in range(4, 0, -1):
    idleLeft += [pygame.transform.flip(pygame.image.load('pildid\Idle\cuphead_idle_' + str(i) + '.png'), True, False)]

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idleCount = 0
        self.standing = True
        self.hitbox = (self.x, self.y, 130, 150)
        self.health = 3
        self.dashing = False


    def draw(self, window):

        if self.walkCount + 1 >= 48:
            self.walkCount = 0

        if self.idleCount + 1 >= 27:
            self.idleCount = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(idleRight[self.idleCount // 3], (self.x, self.y))
                self.idleCount += 1
            else:
                window.blit(idleLeft[self.idleCount // 3], (self.x, self.y))
                self.idleCount += 1
        self.hitbox = (self.x, self.y, 130, 150)
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)

    def hit(self, window):
        self.isJump = False
        self.jumpCount = 10
        self.x = 200
        self.y = 500
        self.walkCount = 0
        self.idleCount = 0
        font1 = pygame.font.SysFont('comicsans',100)
        text = font1.render('Health: -1', 1, (255,255,255))
        window.blit(text, (1280/2 - (text.get_width()/2), 720/2 - (text.get_height()/2)))
        pygame.display.update()
        i = 0
        while i < 50:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 51
                    pygame.quit()

    def dash(self, facing):
        self.x += 200 * facing