# This file was created by Nathan Cayanes
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame videogame series
# Video link: https://youtu.be/OmlQ0XCvIn0

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sound')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,25):
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update
            self.draw
    def update(self):
            # update all sprites
            self.all_sprites.update()
            # this is what prevents the player from falling through the platform when falling down...
            if self.player.vel.y > 0:
                    hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                    if hits:
                        if hits[0].kind == "bouncy":
                            self.player
                        else:
                            self.player.pos.y = hits[0].rect.top
                            self.player.vel.y = 0
                        
            # this prevents the player from jumping up through a platform
            if self.player.vel.y < 0:
                hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
                if hits:
                    print("ouch")
                    SCORE -= 1
                    if self.player.rect.bottom >= hits[0].rect.top - 5:
                        self.player.rect.top = hits[0].rect.bottom
                        self.player.acc.y = 5
                        self.player.vel.y = 0
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                self.running = False
    def draw(self):
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while g.run:
    g.new()

pg.quit()