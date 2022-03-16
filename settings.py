import pygame as pg

# culori (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (100, 0, 0)   # dark red
YELLOW = (255, 255, 0)
BLUE = (0, 0, 225)

# game settings
WIDTH = 728
HEIGHT = 728
FPS = 60
TITLE = "My game"
BGCOLOR = DARKGREY

TILESIZE = 52
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#fontul pt afisarea scorului
pg.init()
font = pg.font.SysFont("arial",30)
pct = 0


