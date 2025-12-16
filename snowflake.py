import turtle


def setup(
    pencil,
):  # задача функции setup - задать цвет черепашки(pencil) и переместить ее в позицию, в которой рисование будет более центрированным
    pencil.color("blue")
    pencil.penup()
    pencil.goto(-200, 100)
    pencil.pendown()


def koch(pencil, size, order):
    if (
        order == 0
    ):  # простейший случай: если аргумент order равен 0 рисуем прямую линию длиной size
        pencil.forward(size)
    else:  # в противнойм случае вызываем функцию koch() четыре раза передавая ей аргумент size деленный на 3 и уменьшая аргумент order на единицу
        for angle in [60, -120, 60, 0]:
            koch(pencil, size / 3, order - 1)
            pencil.left(
                angle
            )  # после каждого вызова функции koch() меняем угол движения черепашки


#
def main():  # функция main создает черепашку (обьект pencil) определяет две переменные order and size и вызывает рекурсивную функцию передавая ей три аргумента
    pencil = turtle.Turtle()
    setup(pencil)
    turtle.tracer(100)

    order = 5
    size = 400

    for i in range(
        3
    ):  # вызываем функцию koch() три раза, каждый раз поварачивая перо на 120º
        koch(pencil, size, order)
        pencil.right(120)


if __name__ == "__main__":
    main()  # вызываем функцию main() и проверяем чтобы была запущенна функция mainloop() модуля turtle
    turtle.tracer(100)  # функция tracer() увиличивает скорость черепашки
    turtle.mainloop()
