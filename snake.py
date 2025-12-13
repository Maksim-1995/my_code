import pygame as pg
from random import randrange

# Рабочее окно
RES = 600
SIZE = 20

# Инициализация змейки и яблока
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

# Запретить змейке движение назад (теперь для стрелок)
dirs = {
    'UP': True,
    'DOWN': True,
    'LEFT': True,
    'RIGHT': True,
}

length = 1
snake = [(x, y)]
# направление движения
dx, dy = 0, 0
score = 0
fps = 8  # Немного увеличил начальную скорость для лучшей реакции

# Инициализируем модуль pygame
pg.init()
# Создать рабочее окно
sc = pg.display.set_mode([RES, RES])
pg.display.set_caption('Snake Game')
# Создадим объект класса Clock для регулирования скорости змейки
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 26, bold=True)
font_end = pg.font.SysFont('Arial', 66, bold=True)
font_small = pg.font.SysFont('Arial', 20, bold=True)

try:
    img = pg.image.load('2.png').convert()
except:
    # Если картинки нет, создаем простой фон
    img = pg.Surface((RES, RES))
    img.fill((30, 30, 30))

# Переменная для управления игровым циклом
running = True
# Флаг для отслеживания, двигалась ли уже змейка
game_started = False

while running:
    # Обработка событий в начале цикла
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        # Обработка нажатий клавиш через события (более точный контроль)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and dirs['UP']:
                dx, dy = 0, -1
                dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
                game_started = True
            elif event.key == pg.K_DOWN and dirs['DOWN']:
                dx, dy = 0, 1
                dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                game_started = True
            elif event.key == pg.K_LEFT and dirs['LEFT']:
                dx, dy = -1, 0
                dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
                game_started = True
            elif event.key == pg.K_RIGHT and dirs['RIGHT']:
                dx, dy = 1, 0
                dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
                game_started = True
    
    # Если игра еще не началась, показываем инструкцию
    if not game_started:
        sc.blit(img, (0, 0))
        # Отображение инструкции
        instruction = font_small.render('USE ARROW KEYS TO START', 1, pg.Color('yellow'))
        sc.blit(instruction, (RES // 2 - 150, RES // 2))
        pg.display.flip()
        clock.tick(5)  # Низкий FPS при ожидании старта
        continue
    
    # Движение змейки (только если игра началась)
    x += dx * SIZE
    y += dy * SIZE
    
    # Каждый шаг змейки будем добавлять в ее список координат
    snake.append((x, y))
    # Сделаем змейку необходимого размера
    snake = snake[-length:]
    
    # Отображение
    sc.blit(img, (0, 0))
    
    # Рисуем змейку (голова другим цветом)
    for idx, (i, j) in enumerate(snake):
        if idx == len(snake) - 1:  # Голова
            pg.draw.rect(sc, pg.Color('lime'), (i, j, SIZE - 2, SIZE - 2))
        else:  # Тело
            pg.draw.rect(sc, pg.Color('green'), (i, j, SIZE - 2, SIZE - 2))
    
    # Рисуем яблоко
    pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE - 2, SIZE - 2))
    
    # Рендерим счет
    render_score = font_score.render(f'SCORE: {score}', 1, pg.Color('orange'))
    sc.blit(render_score, (5, 5))
    
    # Поедание яблока
    if snake[-1] == apple:
        # Генерация нового яблока, которое не попадает на змейку
        attempts = 0
        while True:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            if apple not in snake:
                break
            attempts += 1
            if attempts > 100:  # Защита от бесконечного цикла
                break
        
        # После поедания увеличиваем длину змейки и счет
        length += 1
        score += 1
        # Умеренное увеличение скорости
        if score % 5 == 0:  # Увеличиваем скорость каждые 5 яблок
            fps += 1
    
    # Определение проигрыша
    game_over = False
    # Проверка столкновения со стенами
    if x < 0 or x >= RES or y < 0 or y >= RES:
        game_over = True
    
    # Проверка столкновения с собой (кроме головы)
    if len(snake) != len(set(snake)):
        game_over = True
    
    # Обработка конца игры
    if game_over:
        end_loop = True
        while end_loop:
            # Очистка экрана
            sc.fill(pg.Color('black'))
            sc.blit(img, (0, 0))
            
            # Отображение змейки и яблока (последний кадр)
            for idx, (i, j) in enumerate(snake):
                if idx == len(snake) - 1:
                    pg.draw.rect(sc, pg.Color('darkred'), (i, j, SIZE - 2, SIZE - 2))
                else:
                    pg.draw.rect(sc, pg.Color('darkgreen'), (i, j, SIZE - 2, SIZE - 2))
            pg.draw.rect(sc, pg.Color('red'), (*apple, SIZE - 2, SIZE - 2))
            
            # Сообщение о конце игры
            render_end = font_end.render('GAME OVER', 1, pg.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 4))
            
            # Отображение финального счета
            render_final_score = font_score.render(f'FINAL SCORE: {score}', 1, pg.Color('orange'))
            sc.blit(render_final_score, (RES // 2 - 100, RES // 2))
            
            # Инструкция для выхода
            render_instruction = font_small.render('Press SPACE to restart or ESC to quit', 1, pg.Color('white'))
            sc.blit(render_instruction, (RES // 2 - 180, RES // 1.5))
            
            # Подсказка управления
            controls = font_small.render('Controls: ARROW KEYS', 1, pg.Color('cyan'))
            sc.blit(controls, (RES // 2 - 100, RES // 1.3))
            
            pg.display.flip()
            
            # Обработка событий в меню конца игры
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit()
                    if event.key == pg.K_SPACE:
                        # Рестарт игры
                        x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                        dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                        length = 1
                        snake = [(x, y)]
                        dx, dy = 0, 0
                        score = 0
                        fps = 8
                        game_started = False  # Ждем первого нажатия
                        end_loop = False
                        break
    
    # Обновляем поверхность
    pg.display.flip()
    # Задаем FPS
    clock.tick(fps)

pg.quit()
