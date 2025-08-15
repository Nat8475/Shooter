import pygame as pg
from Menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(1280, 920))

    def run(self):
        print("The Game has Started")
        
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
            #todo Check all Events

            # for event in pg.event.get(): 
                
            #     #* Close Game
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         quit()







