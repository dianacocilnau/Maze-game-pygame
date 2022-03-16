import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    pct = 0
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)#cand tinem apasata o tasta de miscare, player ul nostru se va miscqa incontinuu
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initializam toate variabilele si facem setup-ul pentru noul joc
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.monsters = pg.sprite.Group()
        self.treasure = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':#peretii sunt reprezentati de 1 in mapa noastra(map.txt)
                    Wall(self, col, row)
                if tile == 'P':# punctul de spawn este reprezentat de P in mapa noastra(map.txt)
                    self.player = Player(self, col, row)
                if tile == 'm': #monstru
                    Monster(self, col, row)
                if tile == 'c': #comoara
                    Treasure(self, col, row)

    def run(self):
        # loop-ul jocului
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            self.show_score()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # actualizam porțiunea buclei jocului
        self.all_sprites.update()


    #desenare grid
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT)) #am desenat liniiile orizontale din grid
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y)) #am desenat liniile verticale din grid

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        #apasarea tastelor corespunzatoare comenzilor dorite
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if event.key == pg.K_SPACE:
                    self.player.shoot(dx=1)
                    self.player.shoot(dx=-1)
                    self.player.shoot(dy=-1)
                    self.player.shoot(dy=1)

    def show_score(self):
        score = font.render("Score : " + str(self.player.pct), True, (255, 255, 255))
        self.screen.blit(score, (10, 10))
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# jocul in sine
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
    