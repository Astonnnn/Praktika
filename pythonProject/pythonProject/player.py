import pygame
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x_koordinaat = 480
        y_koordinaat = 480
        self.images = []
        for i in range(1, 16):
            img = pygame.image.load(os.path.join('pildid\Run\cuphead_run_' + str(i) + '.png')).convert()
            self.images.append(img)
            self.player = self.images[0]
            self.rect = self.player.get_rect(midbottom=(x_koordinaat, y_koordinaat))
            self.player = pygame.transform.scale(self.player, (150, 150))
