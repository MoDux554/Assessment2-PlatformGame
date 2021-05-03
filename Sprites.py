# Sprites to be called from the main platform file
import pygame as pg
from PlatformerSettings import*
vec = pg.math.Vector2
import time



class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40)) # Sprite is 30 pixels wide and 40 pixels long
        self.image.fill(WHITE) # Makes the sprite blue thanks to the settings file imported
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(0, 150)
        self.vel = vec(0, 0) # Sets the velocity in the x y coordinates
        self.acc = vec(0, 0) # Sets the acceleration in the xy coordinates
        self.jumpenergy = 0
        self.canjump = True
        self.onground = True



    def jump(self):

        #Check for when the player is on a platform so they only jump once
        self.rect.x += 1
        collision = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1

        if collision:
            self.onground = True
        if not collision:
            self.onground = False




    # After the player jumps they will be able to float for a limited amount of time before descending


    def update(self):


        self.acc = vec(0, PLAYER_ASCENDING)
        keys = pg.key.get_pressed()

        # Checks for input
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_HOR_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_HOR_ACC


        if keys[pg.K_SPACE] and self.jumpenergy < 15 and self.canjump:
            self.acc.y = -PLAYER_ASCENDING
            self.jumpenergy += 1

        if self.jumpenergy == 15:
            self.canjump = False

        if self.jumpenergy == 0 and self.canjump == False:
            self.jumpenergy = 0
            self.canjump = True

        if not keys[pg.K_SPACE]:
            self.acc.y = PLAYER_ASCENDING * 1
            self.jumpenergy -= 0.5

        # Friction applied to the player while they are moving horizontally
        self.acc.x += self.vel.x * PLAYER_FRICTION


        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #Gravity

        # When the player reaches the border of the screen they will be back on the other side
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # Makes sure that the position of the player will be at the bottom in the middle of the player
        self.rect.midbottom = self.pos


class Platforms(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BadPlatforms(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Booster(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y