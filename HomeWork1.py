print("Добро пожаловать в программу для выведения фигур!")
print("Если вы хотите вывести треугольник повёрнутый влево, введите 1")
print("Если вы хотите вывести треугольник повёрнутый вправо, введите 2")
print("Если вы хотите вывести треугольник повёрнутый вниз, введите 3")
print("Если вы хотите вывести треугольник повёрнутый вверх, введите 4")
print("Если вы хотите вывести 2 треугольника напротив друг-друга сверху-вниз, введите 5")
print("Если вы хотите вывести 2 треугольника напротив друг-друга слева-направо, введите 6")
n = int(input("Введите выбранное вами число, соответствующее выбранной фигуре: "))
if n == 1:
    for i in range(10, 0, -2):
        print((10 - i) * ' ' + i * '*')
elif n == 2:
    for i in range(0, 10, +2):
        print(i * '*' + (10 - i) * ' ')
elif n == 3:
    b = 10
    for i in range(b, 0, -1):
        num = b - i
        print(' ' * num + '*' * i + '*' * i)
elif n == 4:
    b = 10
    for i in range(b - 1):
        num = b - i
        print(' ' * num + '*' * i + '*' * i)
elif n == 5:
    b = 10
    for i in range(b, 0, -1):
        num = b - i
        print(' ' * num + '*' * i + '*' * i)
    for i in range(b - 1):
        num = b - i
        print(' ' * num + '*' * i + '*' * i)
elif n == 6:
    import turtle

    tur = turtle.Turtle()

    tur.left(90)
    tur.forward(100)
    tur.right(120)
    tur.forward(100)
    tur.right(120)
    tur.forward(100)
    tur.left(180)
    tur.up()
    tur.forward(100)
    tur.down()
    tur.forward(100)
    tur.right(120)
    tur.forward(100)
    tur.right(120)
    tur.forward(100)

    turtle.done()