# эксперемент № 1 получаем звезду, пробуем менять аргументы функции

import turtle

"""
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('red')

for i in range(5):
    slowpoke.forward(300)
    slowpoke.right(144)

turtle.mainloop()

# эксперемент № 2

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.pencolor('blue')
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)

slowpoke.shape('turtle')
slowpoke.pencolor('red')
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(50)

turtle.mainloop()
"""
# эксперемент №3

slowpoke = turtle.Turtle()
slowpoke.shape("turtle")
slowpoke.pencolor("blue")


def make_shape(t, sides):
    angle = 360 / sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)


make_shape(slowpoke, 3)
make_shape(slowpoke, 5)
make_shape(slowpoke, 8)
make_shape(slowpoke, 10)

turtle.mainloop()
