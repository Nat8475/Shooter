import pygame as pg
from Menu import Menu
from Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from Level import Level

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                    level = Level(self.window, "Level1", menu_return)
                    level_return = level.run()
                    

            # if menu_return == MENU_OPTION[1]:
            #     print("Multi COOP")

            # if menu_return == MENU_OPTION[2]:
            #     print("MULTI COMP")

            # if menu_return == MENU_OPTION[3]:
            #     print("Score")

            #? CLOSE THE GAME
            if menu_return == MENU_OPTION[4]:
                quit()
            else:
                pass







