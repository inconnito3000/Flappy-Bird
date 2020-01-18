import pygame
from Settings import *
vec = pygame.math.Vector2

class Bird(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.bird_gravity = 0.8
        self.size = 30
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = height / 2
        self.pos = vec(100, height / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.vel.y = -11

    def update(self):
        self.acc = vec(0, self.bird_gravity)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
