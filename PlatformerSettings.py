# Settings for the game like dimensions and colour
TITLE = "BalloonPlatform"
WIDTH = 1280
HEIGHT = 720
FPS = 60
FONT_NAME = 'arial'
HIGHSCORE_FILE = 'highscore.txt'

SPRITES = "spritesheet_jumper.png"


# Player Properties
PLAYER_HOR_ACC = 0.5
PLAYER_ASCENDING = 0.15
PLAYER_GRAVITY = 0.2
PLAYER_FRICTION = -0.1



# Starting Platforms / List of Platforms
NORMAL_PLATFORM_LIST = [(0, HEIGHT - 60, 150, 40),
                 (250, HEIGHT -200, 200, 15),
                 (700, HEIGHT - 250, 200, 15),
                 (700, HEIGHT - 130, 200, 15),
                 (1200, HEIGHT - 350, 200, 15),
                 (1600, HEIGHT -100, 200, 20),
                 (1900, HEIGHT - 200, 200, 20),
                 (2120, HEIGHT - 300, 200, 20),
                 (1950, HEIGHT - 500, 200, 20),
                 (3100, HEIGHT - 500, 200, 20),
                 (4500, HEIGHT - 150, 200, 20),
                 (4600, HEIGHT - 150,100, 20),
                 (4800, HEIGHT - 150,100, 20),
                 (5100, HEIGHT - 150,100, 20),
                 (5400, HEIGHT - 150,100, 20)]



BAD_PLATFORM_LIST = [(460, HEIGHT-300, 60, 20),
                    (1000, HEIGHT-600, 60, 300),
                    (1000, HEIGHT - 150, 60, 300),
                    (1450, HEIGHT-275, 200, 20),
                    (1815, HEIGHT - 300, 60, 250),
                    (2120, HEIGHT - 500, 60, 250),
                     (4150, HEIGHT - 150, 200,20)]




HBOOSTER_PLACEMENTS = [(2500,HEIGHT - 550, 20, 20),
                       (3400, HEIGHT - 300, 20, 20),
                       (3600, HEIGHT - 300, 20, 20),
                       (3800, HEIGHT - 300, 20, 20),
                       (4750,  HEIGHT - 150, 20, 20),
                       (5000, HEIGHT - 150, 20, 20),
                       (5300, HEIGHT - 150, 20, 20)]

VBOOSTER_PLACEMENTS =[(4200, HEIGHT - 300, 20, 20)]

V2BOOSTER_PLACEMENTS =  [(5400, HEIGHT - 150,20, 20)]





# Defining colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

