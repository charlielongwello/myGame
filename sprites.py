# This file was created by: charlie longwello
import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'pixel guy.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
        # the players health/hitpoints is 50
        self.hitpoints = 50
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
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
        # when the player collides with the mob the mob disspears 
        mobcollide = pg.sprite.spritecollide(self, self.game.all_mobs, True)
        if mobcollide:
            # each mob when collides with player it does 10 damage
            self.hitpoints -= 10
            # when the player dies and the hitpoints run 0 the player dissapears
        if self.hitpoints == 0:
            self.image.fill(BLACK)

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        # Added new image for the platforms
        self.image = pg.image.load(os.path.join(img_folder, 'stone.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        # makes the platforms move "moving"
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        



# new mobs (add more ghosts)

# Mob sprite, also known as the enemy.
class Mob(Sprite):
    def __init__(self, game, x, y, w, h, kind):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        # changed mob image to ghost from mario
        self.image = pg.image.load(os.path.join(img_folder, 'marioghost.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
    
        

    # this chunk of code defines the enemy/mob seeking in the game
    def seeking(self):
            if self.rect.x < self.game.player.rect.x:
                self.rect.x +=1
            if self.rect.x > self.game.player.rect.x:
                self.rect.x -=1
            if self.rect.y < self.game.player.rect.y:
                self.rect.y +=1
            if self.rect.y > self.game.player.rect.y:
                self.rect.y -=1
    def update(self):
         self.seeking()
       
class Cross(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'pixelcross.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
 
    def update(self):
        self.rect.midbottom = self.pos