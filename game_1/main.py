import pygame as pg

from settings import *

from player import Player

import math


pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
player = Player()


while True:
    for event in pg.event.get():
        # Проверим все события и выход из приложения
        if event.type == pg.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    # Рисуем игрока.
    pg.draw.circle(sc, GREEN, player.pos, 12)
    # Вычисляем sin и cos игрока.
    pg.draw.line(
        sc,
        GREEN,
        player.pos,
        (
            player.x + WIDTH * math.cos(player.angle),
            player.y + WIDTH * math.sin(player.angle),
        ),
    )

    pg.display.flip()
    clock.tick(FPS)
