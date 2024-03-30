"""


Арнольд Шварценеггер стреляет в ужасного монстра Годзиллу из дробовика. Нужно найти общую величину урона, нанесённого
Годзилле выстрелом.

Подсказка: возможно, для быстрой работы программы вам пригодится алгоритм Евклида.
Формат ввода

Сначала вводится количество дробинок.
Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью, её числитель и знаменатель вводятся на
отдельных строках.
Формат вывода

Суммарный урон, выраженный простой несократимой дробью с дробной чертой между числителем и знаменателем.

"""


def nok(a, b) -> int:
    xa = a
    xb = b
    while a != b:
        if a > b:
            b += xb
        else:
            a += xa
    return a


def nod(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


n = int(input())
chislitel_first = int(input())
znamenatel_first = int(input())
for el in range(n - 1):
    chislitel_second = int(input())
    znamenatel_second = int(input())
    znamenatel = nok(znamenatel_first, znamenatel_second)
    chislitel_first = (chislitel_first * znamenatel // znamenatel_first) + (chislitel_second * znamenatel
                                                                            // znamenatel_second)
    znamenatel_first = znamenatel
delit = nod(chislitel_first, znamenatel_first)
print(f'{chislitel_first // delit}/{znamenatel_first // delit}')
