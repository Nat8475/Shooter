import random
import sys
import pygame as pg
from pygame import Rect, Surface
from pygame.font import Font
from Const import C_PURPLE, C_GREEN, C_WHITE, ENEMY_SPAWN_TIME, EVENT_ENEMY, EVENT_TIMEOUT, TIMEOUT_STEP, WIN_HEIGHT, FPS, MENU_OPTION, TIMEOUT_GAME
from Enemy import Enemy
from Entity import Entity
from Player import Player
from entityFactory import entityFactory
from EntityMediator import EntityMediator

class Level():
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.timeout = TIMEOUT_GAME
        

        #o RANDOM BACKGROUND AND LOAD
        choiceBG = random.choice(('Level1Bg', 'Level2Bg'))
        self.entity_list.extend(entityFactory.get_entity(choiceBG))

        #o DRAW PLAYER 1
        player = entityFactory.get_entity('Player1')
        player.score = player_score[0]

        self.entity_list.append(player)
        
        #o DRAW PLAYER 2

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = entityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        #o SET TIME TO SPAWN ENTITYS 

        pg.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

        #o LEVEL 2

        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):

        #o LOAD MUSIC LEVEL

        pg.mixer_music.load(f'./assets/Level.wav')
        pg.mixer_music.play(-1)

        clock = pg.time.Clock()

        while True:

            #o FPS

            clock.tick(FPS)

            #o DRAW ENTITYS
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest= ent.rect)
                ent.move()

                #o DRAW SHOT PLAYER AND ENEMY
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)


                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10,20))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_PURPLE, (10,30))
                

            #o ALL EVENTS

            for event in pg.event.get():

                #* CHECK CLOSE WINDOW

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                #* CHECK ENEMY RANDOW SPAWN

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(entityFactory.get_entity(choice))
                
                #* CHECK TIMEOUT FASES AND SCORE

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1': player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2': player_score[1] = ent.score
                        return True
                    
                #* CHECK PLAYER DEATH

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False
    


            #o DRAW TEXT IN LEVEL

            
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10,5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
        
            pg.display.flip()

            #o VERIFY COLLISION AND DELET ENTITYS

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)
