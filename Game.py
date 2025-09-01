import pygame as pg
from Menu import Menu
from Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from Level import Level
from Score import Score

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            score = Score(self.window)


            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                    player_score = [0, 0] # [Player1, Player2]

                    # pg.mixer_music.load(f'./assets/SelectMenu.mp3')
                    # pg.mixer_music.play(1)

                    level_names = ['level_1', 'level_2', 'level_3']

                    for level_name in level_names:
                        level = Level(self.window, level_name, menu_return, player_score)
                        level_return = level.run(player_score)

                        if not level_return:
                            break

            # if menu_return == MENU_OPTION[3]:
            #     print("Score")

            #? CLOSE THE GAME
            if menu_return == MENU_OPTION[4]:
                quit()
            else:
                pass