# this file was created by charlie longwello

# game settings 
# changed screen settings to make the game larger
WIDTH = 1024
HEIGHT = 768
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 2
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (92, 59, 0)
BLUE = (0, 0, 0)


# adds different platforms into the game
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (175, 100, 50, 20, "normal"),
                 (234, 200, 50, 20, "normal")]
                

