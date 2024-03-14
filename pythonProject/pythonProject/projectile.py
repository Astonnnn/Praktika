import pygame

height = 50
width = 77

kuulid = [pygame.transform.scale(pygame.image.load("pildid\projectile\kuul1.PNG"), (width,height)),
          pygame.transform.scale(pygame.image.load("pildid\projectile\kuul2.PNG"), (width,height)),
          pygame.transform.scale(pygame.image.load("pildid\projectile\kuul3.PNG"), (width,height)),
            pygame.transform.scale( pygame.image.load("pildid\projectile\kuul4.PNG"), (width,height))]


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 12 * facing
        self.imageCount = 0

    def draw(self, window):
        if self.facing == 1:
            if self.imageCount < 3:
                window.blit(kuulid[0], (self.x, self.y))
            elif self.imageCount < 6:
                window.blit(kuulid[1], (self.x, self.y))
            elif self.imageCount < 9:
                window.blit(kuulid[2], (self.x, self.y))
            elif self.imageCount < 12:
                window.blit(kuulid[3], (self.x, self.y))
            else:
                self.imageCount = 0
                window.blit(kuulid[0], (self.x, self.y))


        else:
            if self.imageCount < 2:
                window.blit(pygame.transform.flip(kuulid[0],True,False), (self.x-100, self.y))
            elif self.imageCount < 4:
                window.blit(pygame.transform.flip(kuulid[1],True,False), (self.x-100, self.y))
            elif self.imageCount < 6:
                window.blit(pygame.transform.flip(kuulid[2],True,False), (self.x-100, self.y))
            elif self.imageCount < 8:
                window.blit(pygame.transform.flip(kuulid[3],True,False), (self.x-100, self.y))
            else:
                self.imageCount = 0
                window.blit(pygame.transform.flip(kuulid[0], True, False), (self.x - 100, self.y))


        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

