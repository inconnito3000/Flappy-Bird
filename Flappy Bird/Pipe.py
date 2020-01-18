import pygame
import random
from Settings import *

class Bottom_Pipe(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.height = 250
        self.game = game
        self.speed = 5.5
        self.image = pygame.Surface((self.game.bird.size, self.height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width * 2 , self.game.ground.rect.top)

    def reset_size(self):
        self.height = random.randint(75, 250)
        self.image = pygame.Surface((self.game.bird.size, self.height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width + 90 , self.game.ground.rect.top)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right <= 0:
            self.rect.centerx = width + 90
            self.reset_size()


class Top_Pipe(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.height = 250
        self.game = game
        self.speed = 5.5
        self.image = pygame.Surface((self.game.bird.size, self.height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.midtop = (width * 2, 0)

    def reset_size(self):
        self.height = (600 - self.game.pipe_down.height) - 170
        self.image = pygame.Surface((self.game.bird.size, self.height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.midtop = (width + 90, 0)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right <= 0:
            self.rect.centerx = width + 90
            self.reset_size()
