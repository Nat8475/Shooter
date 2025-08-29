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
                    player_score = [0, 0] # [Player1, Player2]

                    # pg.mixer_music.load(f'./assets/SelectMenu.mp3')
                    # pg.mixer_music.play(1)

                    # level = Level(self.window, "Level1", menu_return)
                    # level_return = level.run()
                    # if level_return:
                    #     level = Level(self.window, "Level2", menu_return)
                    #     level_return = level.run()
                        
                    level_number = 1
                    #levels = ["Level1", "Level2", "Level3", "Level4"]  # Adicione quantos níveis quiser aqui
                    while True:
                        level_name = f'Level{level_number}'
                        
                        level = Level(self.window, level_name, menu_return, player_score)
                        level_return = level.run(player_score)

                        level_number += 1
                        if not level_return:
                            break # O jogo parou (o jogador perdeu ou saiu)
                    

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