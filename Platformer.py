#Game Template
import pygame as pg
import random
from PlatformerSettings import*

class Game():
    def __init__(self):
        # Initializes pygame and creates the window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.gameRunning = True

    def new(self):
    #starting a new game
        self.sprites = pg.sprite.Group()
        self.run()

    def run(self):
    #when the game is running/game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()


    def update(self):
    #for the gameto update
        self.sprites.update()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False #stops the game running loop and ends the game

    def draw(self):
        # drawing on the screen
        self.screen.fill(BLACK)
        self.sprites.draw(self.screen)
        # this comes after drawing all the time
        pg.display.flip()


    def game_start_screen(self):
        pass

    def gameover_screen(self):
        pass


game = Game()
game.game_start_screen()
while game.gameRunning :
    game.new()
    game.game_start_screen()
pg.quit()

