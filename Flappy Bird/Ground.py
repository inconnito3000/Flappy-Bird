import pygame
from Settings import *

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 100))
        self.image.fill(brown)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width / 2, height)