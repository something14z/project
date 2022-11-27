import pygame as pg
import sys
from Settings import*
from Map import*
class Player():
    def __init__(self, inv, is_alive, stamina, location):
        self.inv = []
        self.is_alive = True
        self.stamina = stamina
        self.location = location

    def move_up(self):
        self.location += 1
        self.stamina - 5

    def move_down(self):
        self.location -= 1

    def render_check(self, location):
        if self.location > 0:
            if self.location == len(Map.Map.mapup):
                pass

        elif self.location < 0:
            if self.location == len(Map.Map.mapdown):
                Map.Map.genetratedown()

class Game :
    def __init__(self):
        pg.init()
        self.screen = pg .display.set_mode(RES)
        self.clock = pg.time.Clock()

    def draw_menu(self,on):
        pg.init()
        screen = pg.display.set_mode([500, 500])
        while on:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
            screen.fill((255, 0, 0))
            pg.display.flip()
    def new_game (self):
        pass

    def update (self):
        pg.display.flip
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill("black")

    def game_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


    def game_run (self):
        while True:
            self.game_events()
            self.update()
            self.draw()

menu_on = True
if __name__ == '__main__':
    main = Game()
    if menu_on:
        main.draw_menu(menu_on)
    else:
        main.game_run()