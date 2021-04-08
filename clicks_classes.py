import pygame
from random import *

class Circle(pygame.sprite.Sprite):
    def __init__(self, surf_list, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = choice(surf_list)
        x = randint(100, 500)
        y = randint(100, 300)
        self.rect = self.image.get_rect(
            center=(x,y))
        self.r = min(self.rect.w, self.rect.h) // 2
        self.add(group)
