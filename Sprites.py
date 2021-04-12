# Sprites to be called from the main platform file
import pygame as pg
from PlatformerSettings import*
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40)) # sprite is 30 pixels wide and 40 pixels long
        self.image.fill(BLUE) # makes the sprite blue thanks to the settings file imported
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()

        # Checks for input
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Friction applied to the player
        self.acc += self.vel * PLAYER_FRICTION

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # When the player reaches the border of the screen they will be back on the other side
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # Makes sure that the centre of the sprite is in the same place as the current position
        self.rect.center = self.pos
