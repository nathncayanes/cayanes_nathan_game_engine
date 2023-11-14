# This file was created by: Nathan Cayanes
# Base code from Chris Bradfield and his content on Kids Can Code: http://kidscancode.org/blog/
# Code for Player 2 Class from Mr. Cozort's Game

'''
Goals:
add an ice platform, DONE
add more colors, DONE
make the mobs "coins" that add up to your score, DONE but couldn't find out how to add an image on it
add a second player and make it a race to the top, DONE
add a finish line for the race, DONE
'''

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
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.ice_platforms = pg.sprite.Group()
        self.finishline = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        self.player2 = Player2(self)
        # add instances to groups
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for i in ICEPLATFORM_LIST:
            # instantiation of the Ice Platform class
            iceplat = IcePlat(*i)
            self.all_sprites.add(iceplat)
            self.ice_platforms.add(iceplat)

        for c in FINISHLINE_LIST:
            # instantiation of the Finishline class
            finplat = FinishLine(*c)
            self.all_sprites.add(finplat)
            self.finishline.add(finplat)

        # instantiates the mob class
        for m in range(0,10):
            # the range and randint statement makes it so that the mobs spawn in random places
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

        self.run()
    # begins the pygame clock "starting up" the game
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    # updates the "drawing" of all_sprites on the popup
    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down
        # this code is taken from Mr. Cozort's Pygame example
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5
        # this just replicates the same effect for the second player
        if self.player2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player2, self.all_platforms, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top
                self.player2.vel.y = 0
                self.player2.vel.x = hits[0].speed*1.5
                    
         # this prevents the player from jumping up through a platform
        if self.player.vel.y != 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                if self.player.vel.y > 0:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            # this unlike the top one is only for ice_platforms and because it doesn't include the friction code
            # in all_platforms, it creates a "slippery" effect
            slips = pg.sprite.spritecollide(self.player, self.ice_platforms, False)
            if slips:
                if self.player.vel.y > 0:
                    self.player.pos.y = slips[0].rect.top
                    self.player.vel.y = 0
        # this replicates the code from above but for the second player
        if self.player2.vel.y != 0:
            hits = pg.sprite.spritecollide(self.player2, self.all_platforms, False)
            if hits:
                if self.player2.vel.y > 0:
                    self.player2.pos.y = hits[0].rect.top
                    self.player2.vel.y = 0
            slips = pg.sprite.spritecollide(self.player2, self.ice_platforms, False)
            if slips:
                if self.player2.vel.y > 0:
                    self.player2.pos.y = slips[0].rect.top
                    self.player2.vel.y = 0

        # this set of code makes it the game like "doodle jump" and gradually moves the screen up
        if self.player.pos.y < HEIGHT:
            for p in self.all_platforms:
                p.rect.y += 1

        if self.player.pos.y < HEIGHT:
            for p in self.ice_platforms:
                p.rect.y += 1

        if self.player2.pos.y < HEIGHT:
            for p in self.all_platforms:
                p.rect.y += 1

        if self.player2.pos.y < HEIGHT:
            for p in self.ice_platforms:
                p.rect.y += 1

    # this code makes it so that if I close the window the game will stop running
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        # this creates and updates the score on the screen
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        self.draw_text("Whoever reaches the final platform first WINS", 18, WHITE, WIDTH/2, HEIGHT/10 - 25)
        self.draw_text("HINT: hold down space after getting onto the first platform", 15, WHITE, WIDTH/2, HEIGHT/10 -50)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
