'''Объявление игрока в отдельном файле для удобства.'''

from settings import *

import pygame as pg

class Player:
    def __init__(self) -> None:
        self.x, self.y = player_pos
        self.angle = player_angle

    # Свойство которое вернет позицию по x, y.
    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        '''Oтслеживает нажатые клавиши и управляет игроком.'''
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= player_speed
        if keys[pg.K_s]:
            self.y += player_speed
        if keys[pg.K_a]:
            self.x -= player_speed
        if keys[pg.K_d]:
            self.x += player_speed
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02