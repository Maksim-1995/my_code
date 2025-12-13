import pygame as pg
from random import randrange

# Рабочее окно
RES = 600
SIZE = 20

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
# Запретить змейки движение назад.
dirs = {
    'W': True,
    'S': True,
    'A': True,
    'D': True,
}
length = 1
snake = [(x, y)]
# направление движения
dx, dy = 0, 0
score = 0
fps = 5

# Инициализируем модуль pygame
pg.init()
# Создать рабочее окно
sc = pg.display.set_mode([RES, RES])
# Создадим обьект класса clok для регулирования скорости змейки
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 26, bold=True)
font_end = pg.font.SysFont('Arial', 66, bold=True)
img = pg.image.load('2.png').convert()

while True:
    sc.blit(img, (0, 0))
    # Используем списковые включения для краткости
    [
        (pg.draw.rect(sc, pg.Color('green'), (i, j, SIZE - 2, SIZE - 2)))
        for i, j in snake
    ]

    pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE, SIZE))
    # зарендерим надпись ОЧКИ
    render_score = font_score.render(f'SCORE: {score}', 1, pg.Color('orange'))
    sc.blit(render_score, (5, 5))
    # Определим движение змейки с расстоянием равной ее головы
    x += dx * SIZE
    y += dy * SIZE
    # Каждый шаг змейки будем добавлять в ее список координат
    snake.append((x, y))
    # Сделаем змеку необходимиго размера.
    snake = snake[-length:]
    # Поедание яблока.
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        # После поедания увеличиваем скорость и длинну змейки
        length += 1
        score += 1
        fps += 1

    # Определим случай пройгрыша.
    # Змейка вышла за пределы экрана или съела сама себя.
    if (
        x < 0
        or x > RES - SIZE
        or y < 0
        or y > RES - SIZE
        or len(snake) != len(set(snake))
    ):
        while True:
            render_end = font_end.render('GAME OVER', 1, pg.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            # Проверка на закрытие приложения.
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

    # Обновляем поверхность
    pg.display.flip()
    # Задаем задержку для fps
    clock.tick(fps)

    # Закрытие приложения
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # информация о всех нажатых клавишах
    key = pg.key.get_pressed()
    # Переключаем на стандартные кнопки
    if key[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {
            'W': True,
            'S': False,
            'A': True,
            'D': True,
        }
    if key[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {
            'W': False,
            'S': True,
            'A': True,
            'D': True,
        }
    if key[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {
            'W': True,
            'S': True,
            'A': True,
            'D': False,
        }
    if key[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {
            'W': True,
            'S': True,
            'A': False,
            'D': True,
        }
