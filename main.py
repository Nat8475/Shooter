import pygame as pg

pg.init()

print("The Game has Started")
window = pg.display.set_mode(size=(1280, 920))

while True:
    #todo Check all Events

    for event in pg.event.get(): 
        
        #* Close Game
        if event.type == pg.QUIT:
            pg.quit()
            quit() ;;;;;aaaaaa





