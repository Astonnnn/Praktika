import pygame

walkRight = []

for i in range(1,6):
    walkRight += [pygame.transform.scale(pygame.image.load("pildid\enemy\enemy" + str(i) + ".jpg"), (130, 150))]


walkLeft = []
for i in range(1,6):
    walkLeft += [pygame.transform.flip(pygame.transform.scale(pygame.image.load("pildid\enemy\enemy" + str(i) + ".jpg"), (130, 150)), True, False)]


class Enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height= height
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x - 10, self.y, 130, 150)
        self.health = 20
        self.visible = True

    def draw(self, window, characterx):
        self.move(characterx)
        if self.visible:
            if self.walkCount + 1 >= 15:
                self.walkCount = 0

            if self.vel > 0:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0] + 30, self.hitbox[1]-20, 100, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0] + 30, self.hitbox[1]-20, 100 - ((100/20)*(20-self.health)), 10))

            self.hitbox = (self.x - 10, self.y, 90, 103)

            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move(self, target):
        if self.vel > 0:
            if self.x < target:
                self.x += self.vel
            else:
                self.x -= self.vel
                self.walkCount = 0
        else:
            if self.x - self.vel > self.x:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1


