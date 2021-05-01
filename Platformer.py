# Game Template
import pygame as pg
import random
from PlatformerSettings import *
from Sprites import *



class Game():
    def __init__(self):
        # Initializes pygame and creates the window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.gameRunning = True
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        # Starting a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # Creating a new player sprite from the sprites file
        self.player = Player(self)
        self.all_sprites.add(self.player)

        # Adds the platforms from the list in Platformer Settings
        for plat in PLATFORM_LIST:
            p = Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # when the game is running/game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # For the game to update
        self.all_sprites.update()

        # Prevents the player from clipping through platforms underneath
        if self.player.vel.y > 0:
            # Collision check between the player and platforms
            collision = pg.sprite.spritecollide(self.player, self.platforms, False)
            if collision:
                # the player's y position will be set to the top part of the platform
                self.player.pos.y = collision[0].rect.top
                self.player.vel.y = 0

        if self.player.rect.right >= 2 * WIDTH / 3:
            self.player.pos.x -= max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.right -= max(abs(self.player.vel.x), 2)
        if self.player.rect.left <= WIDTH - 300:
            self.player.pos.x += max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.right += max(abs(self.player.vel.x), 2)


        # Game Over Condition
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                # makes it look like the platforms are scrolling down
                sprite.rect.y -= max(self.player.vel.y, 10)
                #removes all the sprites
                if sprite.rect.bottom < 0:
                    sprite.kill()
        #restarts the game
        if len (self.platforms) == 0:
            self.playing = False


    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False  # stops the game running loop and ends the game
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # drawing on the screen
        self.screen.fill(GREY)
        self.all_sprites.draw(self.screen)
        # This comes after drawing all the time
        pg.display.flip()

    def game_start_screen(self):
        self.screen.fill(GREY)
        self.drawtext(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.drawtext("Use left and right arrow keys for movement.", 22, WHITE, WIDTH/2, HEIGHT/ 2)
        self.drawtext("Press and hold the space bar to float for a limited amount of time.", 22, WHITE,WIDTH/ 2, HEIGHT / 3)
        self.drawtext("Press any key to play.",22, WHITE, WIDTH / 2, HEIGHT *3 /4)
        pg.display.flip()
        self.waitforinput()

    def waitforinput(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.gameRunning = False
                if event.type == pg.KEYUP:
                    waiting = False


    def gameover_screen(self):
        pass

    def drawtext(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


game = Game()
game.game_start_screen()
while game.gameRunning:
    game.new()
    game.game_start_screen()
pg.quit()
