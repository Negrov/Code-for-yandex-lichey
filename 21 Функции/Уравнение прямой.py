"""


Как известно, через любые две различные точки на плоскости проходит прямая, и только одна. Напишите функцию
equation(a, b), которая по двум заданным точкам находит уравнение прямой, проходящей через них.

В функцию передаются две строки — координаты точек в формате x;y, функция должна выводить на экран два числа через
пробел — коэффициенты k и b найденной прямой.

Если в решении получается прямая вида y=c или x=c, функция должна печатать эту константу с.

"""


def equation(first_point, second_point):
    x1, y1 = map(float, first_point.split(';'))
    x2, y2 = map(float, second_point.split(';'))

    if x1 == x2 and y1 != y2:
        print(0.0)

    elif x1 != x2 and y1 == y2:
        print(f'{y1}')

    else:
        k = (max(y1, y2) - min(y1, y2)) / (max(x1, x2) - min(x1, x2))
        if x1 > x2 and y2 > y1:
            k = -k
        b = y1 - k * x1
        print(f'{k} {b}')
