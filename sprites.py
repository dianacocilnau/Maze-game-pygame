import pygame as pg
from settings import *

arr = [0, 0, 0]  #Agentul explorator primeste un vector de 3 elemente la fiecare mutare

class Player(pg.sprite.Sprite):
    pct = 0
    ok = 0
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
            arr[0] = 0
            self.pct += -1
        else:
            arr[0] = 1
            self.pct += -1

        if self.collide_with_monsters():
                arr[1] = 1 #jocul se termina cand intram in celula unui monstru
                self.pct += -1000
                self.pct += -1
                self.kill()
                pg.quit()
                print('game over')
                print("score: ", self.pct)
                print(arr)
        else:
            arr[1] = 0

        if self.collide_with_treasure():
               arr[2]=1
               self.ok+=1
               self.pct+= 100
               self.pct += -1 
               if self.ok==3:
                   pg.quit()
                   print('game won')
                   print("score: ", self.pct)
                   print(arr)
        else:
            arr[2] = 0

    def shoot(self, dx=0, dy=0):
        if self.collide_with_monster(dx, dy):
            self.pct += -1

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def collide_with_monsters(self):
        for monster in self.game.monsters:
            if monster.x == self.x and monster.y == self.y :
                return True
        return False

    def collide_with_monster(self, dx=0, dy=0):
        for monster in self.game.monsters:
            if monster.x == self.x + dx and monster.y == self.y + dy:
                self.pct+=50
                self.pct += -1
                monster.kill()
                return True
        return False

    def collide_with_treasure(self):
        for treasure in self.game.treasure:
            if treasure.x == self.x and treasure.y == self.y:
                treasure.kill()
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Monster(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.monsters
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Treasure(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.treasure
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE