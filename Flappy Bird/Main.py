import pygame
import sys
from os import path
from Settings import *
from Pipe import *
from Bird import *
from Ground import *

class Game:
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font('arial')
        self.screen = pygame.display.set_mode((width, height))
        self.title = pygame.display.set_caption(game_title)

        self.score = 0

        self.running = True
        self.playing = True
        self.clock = pygame.time.Clock()

        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, hs_file), 'r') as file:
            try:
                self.highscore = int(file.read())

            except:
                self.highscore = 0
            

    def new(self):
        # Initialise sprite groups.
        self.bird_group = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Initialise bird.
        self.bird = Bird(self)
        self.bird_group.add(self.bird)
        self.all_sprites.add(self.bird)

        # Initialise ground.
        self.ground = Ground()
        self.ground_group.add(self.ground)
        self.all_sprites.add(self.ground)

        # Initialise bottom pipe.
        self.pipe_down = Bottom_Pipe(self)
        self.pipes.add(self.pipe_down)
        self.all_sprites.add(self.pipe_down)

        # Initialise top pipe.
        self.pipe_up = Top_Pipe(self)
        self.pipes.add(self.pipe_up)
        self.all_sprites.add(self.pipe_up)

        self.run()

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.draw()
            self.update()
            self.events()
            self.collision()

    def draw_text(self, surf, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.score), 30, width / 2, 50, light_grey)
        pygame.display.flip()

    def update(self):
        self.all_sprites.update()

        if self.pipe_down.rect.right <= 5:
            self.score += 1

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.bird.jump()

    def game_over(self):
        self.playing = False
        self.running = False
        pygame.quit()
        print("GAME OVER your score is: " + str(self.score))

        if int(self.score) > int(self.highscore):
            print("GAME OVER " + "new highscore: " + str(self.score))
            with open(path.join(self.dir, hs_file), "w") as file:
                file.write(str(self.score))

    def collision(self):
        if self.bird.vel.y >= 0:
            hits = pygame.sprite.spritecollide(self.bird, self.ground_group, False)
            if hits:
                self.bird.pos.y = hits[0].rect.top
                self.bird.vel.y = 0
                self.game_over()

        hits = pygame.sprite.spritecollide(self.bird, self.pipes, False)
        if hits:
            self.game_over()
            pass

        if self.bird.rect.top <= 0:
            pass
            self.game_over()

game = Game()

while game.running:
    game.new()

pygame.quit()
