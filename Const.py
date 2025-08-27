import pygame as pg

#* C
COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255


#* E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 3,
    'Level2Bg5': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

EVENT_ENEMY = pg.USEREVENT + 1

ENEMY_SPAWN_TIME = 4000

#* F
FPS = 100

#*M

MENU_OPTION = [ "New Game 1P", "New Game 2P - COOP", "New Game 2P - COMP", "Score", "Exit" ]

#* P

PLAYER_KEY_UP = {'Player1': pg.K_UP, 'Player2': pg.K_w}
PLAYER_KEY_DOWN = {'Player1': pg.K_DOWN, 'Player2': pg.K_s}
PLAYER_KEY_LEFT = {'Player1': pg.K_LEFT, 'Player2': pg.K_a}
PLAYER_KEY_RIGHT = {'Player1': pg.K_RIGHT, 'Player2': pg.K_d}
PLAYER_KEY_SHOOT = {'Player1': pg.K_RCTRL, 'Player2': pg.K_LCTRL}

#* W
WIN_WIDTH = 576
WIN_HEIGHT = 324
