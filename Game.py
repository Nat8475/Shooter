import pygame as pg
from Menu import Menu
from Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[4]:
                quit()







