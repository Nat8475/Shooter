import random
import sys
import pygame as pg
from pygame import Rect, Surface
from pygame.font import Font
from Const import COLOR_WHITE, ENEMY_SPAWN_TIME, EVENT_ENEMY, WIN_HEIGHT, FPS, MENU_OPTION
from Entity import Entity
from entityFactory import entityFactory

class Level():
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        choiceBG = random.choice(('Level1Bg', 'Level2Bg'))
        
        self.entity_list.extend(entityFactory.get_entity(choiceBG))
        self.entity_list.append(entityFactory.get_entity('Player1'))
        self.timeout = 20000

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(entityFactory.get_entity('Player2'))

        pg.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

        


    def run(self):
        # pg.mixer_music.load(f'./assets/{self.name}.mp3')
        # pg.mixer_music.play(-1)
        clock = pg.time.Clock()

        while True:
            clock.tick(FPS)
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest= ent.rect)
                ent.move()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(entityFactory.get_entity(choice))
            
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
        
            pg.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)
