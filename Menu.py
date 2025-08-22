import pygame as pg
from pygame import Rect, Surface
from pygame.font import Font
from Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('oi.jpg')
        self.rect = self.surf.get_rect(left=0,top=0)

    def run(self):

        menu_option = -1;
        #* Load Music Menu
 
        # pg.mixer_music.load('./assets/Menu.mp3')
        # pg.mixer_music.play(-1)

        while True:
            #* Load Background
            self.window.blit(source=self.surf, dest=self.rect)
            
            #* Write text

            self.menu_text(80, "Mountain Shooter",(COLOR_WHITE), ((WIN_WIDTH/2), 70))
            #self.menu_text(60, "Shooter",(COLOR_ORANGE), ((WIN_WIDTH/2), 100))
            # self.menu_text(35, "New Game 1P",(COLOR_WHITE), ((WIN_WIDTH/8), 200))
            # self.menu_text(35, "New Game 2P - COOP",(COLOR_WHITE), ((WIN_WIDTH/6.25), 250))
            # self.menu_text(35, "New Game 2P - COMP",(COLOR_WHITE), ((WIN_WIDTH/6.25), 300))
            # self.menu_text(35, "Score",(COLOR_WHITE), ((WIN_WIDTH/11.5), 350))
            # self.menu_text(35, "Exit",(COLOR_WHITE), ((WIN_WIDTH/12.5), 400))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(35, MENU_OPTION[i], COLOR_ORANGE,((WIN_WIDTH/8), 200 + 50 * i))
                else:
                    self.menu_text(35, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH/8), 200 + 50 * i))


            


            #* Check all Events
            for event in pg.event.get():
            
            #r Close Game

                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            #r KEYBOARD EVENTS

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1;
                        else:
                            menu_option = 0;
                    
                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1;
                        else:
                            menu_option = len(MENU_OPTION) - 1;
                    
                    if event.key == pg.K_RETURN:
                        return MENU_OPTION[menu_option];
                    
            pg.display.flip()

    def menu_text(self, text_size: int, text: str, text_color:tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)