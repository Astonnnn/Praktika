import pygame
kuul = pygame.image.load("pildid\projectile\kuul1.PNG")
kuul = pygame.transform.scale(kuul, (60,39))


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 12 * facing

    def draw(self, window):
        window.blit(kuul, (self.x, self.y))
        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

