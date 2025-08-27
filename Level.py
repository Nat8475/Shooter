import sys
import pygame as pg
from pygame import Rect, Surface
from pygame.font import Font
from Const import COLOR_WHITE, WIN_HEIGHT, FPS
from Entity import Entity
from entityFactory import entityFactory
from Background import Background

class Level():
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(entityFactory.get_entity('Level1Bg'))
        self.timeout = 20000

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
