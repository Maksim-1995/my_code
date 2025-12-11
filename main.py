import pygame as pg
from random import randrange

# Рабочее окно
RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
# Запретить змейки движение назад.
dirs = {'W': True, 'W': True, 'W': True, 'W': True,}
length = 1
snake = [(x, y)]
# направление движения
dx, dy = 0, 0

fps = 5

# Инициализируем модуль pygame
pg.init()
# Создать рабочее окно
sc = pg.display.set_mode([RES, RES])
# Создадим обьект класса clok для регулирования скорости змейки
clock = pg.time.Clock()

while True:
    sc.fill(pg.Color('black'))
    # Используем списковые включения для краткости
    [(pg.draw.rect(sc, pg.Color('green'),
                   (i, j, SIZE, SIZE))) for i, j in snake]
    
    pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE, SIZE))
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
        fps += 1
        
    # Определим случай пройгрыша.
    # Змейка вышла за пределы экрана.
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        break
    # Змейка сьела себя.
    if len(snake) != len(set(snake)):
        break
        
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
    if key[pg.K_w]:
        dx, dy = 0, -1
    if key[pg.K_s]:
        dx, dy = 0, 1
    if key[pg.K_a]:
        dx, dy = -1, 0
    if key[pg.K_d]:
        dx, dy = 1, 0
        
        
       
    
BN