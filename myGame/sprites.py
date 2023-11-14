import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# determines all the properties of the Player
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        # sets the image used for the character and also takes out all the black in the background
        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        # sets the starting position
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    # defines controls for the player 1
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    # jump logic
    def jump(self):
        # check if it can detect a jump input
        print("trying to jump")
        # makes it so that if the player collides with a platform it can jump
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
        # very similar to above but isntead of a normal platform, ice platforms
        icehits = pg.sprite.spritecollide(self, self.game.ice_platforms, False)
        if icehits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    # 
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        # mob logic, since I set it to True, the coins will disappear
        hits = pg.sprite.spritecollide(self, self.game.all_mobs, True)
        # increases the score when I collide/"collect" coins
        if hits:
            self.game.score += 10
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# player 2 class code from Mr. Cozort's game, basically the same as Player 1's code
class Player2(Player):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -5
        if keys[pg.K_RIGHT]:
            self.acc.x = 5
        if keys[pg.K_UP]:
            self.jump()
    def jump(self): 
        print("trying to jump")
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
        icehits = pg.sprite.spritecollide(self, self.game.ice_platforms, False)
        if icehits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        hits = pg.sprite.spritecollide(self, self.game.all_mobs, True)
        if hits:
            self.game.score += 10
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# platforms

# parent platform class but a child class to Sprites
class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        if self.category == "finish":
            self.image.fill(ORANGE)
# child class to platform class so it takes the same properties as the parent
class IcePlat(Platform):
    def __init__(self, x, y, w, h, category):
        super().__init__(x, y, w, h, category)
        self.image.fill(ICEWHITE)
# child class to platform class so it takes the same properties as the parent
class FinishLine(Platform):
    def __init__(self, x, y, w, h, category):
        super().__init__(x, y, w, h, category)
        self.image.fill(ORANGE)

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        # self.image = pg.image.load(os.path.join(img_folder, 'coin-2.png')).convert()
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
    
    def update(self):
        pass
        