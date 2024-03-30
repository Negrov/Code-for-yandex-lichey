"""
Напишите функцию line(s, t), которая получает на вход две строки: s — уравнение прямой в виде kx+b и t — координаты
точки на плоскости в виде x;y. Ваша программа должна печатать True, если точка лежит на прямой, и False в противном
случае.
"""


def line(equation, point):
    k, b = map(float, equation.split('x'))
    x, y = map(float, point.split(';'))
    print(y == (k * x + b))
