import pygame as pg

class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0,top=0)

    def save_score(self):
        pass

    def show_score(self):

        pg.mixer_music.load('./assets/Score.wav')
        pg.mixer_music.play(-1)

