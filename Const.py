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
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 3,
}

EVENT_ENEMY = pg.USEREVENT + 1

ENEMY_SPAWN_TIME = 3000

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 100
}

#* F
FPS = 100

#*M

MENU_OPTION = [ "New Game 1P", "New Game 2P - COOP", "New Game 2P - COMP", "Score", "Exit" ]

#* P

PLAYER_KEY_UP = {'Player1': pg.K_UP, 'Player2': pg.K_w}
PLAYER_KEY_DOWN = {'Player1': pg.K_DOWN, 'Player2': pg.K_s}
PLAYER_KEY_LEFT = {'Player1': pg.K_LEFT, 'Player2': pg.K_a}
PLAYER_KEY_RIGHT = {'Player1': pg.K_RIGHT, 'Player2': pg.K_d}
PLAYER_KEY_SHOOT = {'Player1': pg.K_RALT, 'Player2': pg.K_LCTRL}

#* W
WIN_WIDTH = 576
WIN_HEIGHT = 324
