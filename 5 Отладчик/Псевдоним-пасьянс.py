"""


Игра Ним с одной кучей для одного игрока с дополнительным ограничением: можно за один ход взять не больше трёх камней.
Игрок может попытаться взять больше трёх камней, меньше одного или больше оставшегося количества, но в этих случаях его
ход игнорируется, и программа ещё раз выводит не изменившееся количество камней.
Формат ввода

В первой строке записано изначальное количество камней в кучке.
Далее следуют несколько целых чисел на отдельных строках — описание ходов игрока.
Формат вывода

В ответ на каждый ход игрока выведите одно число — количество камней в куче после этого хода.

"""


n = int(input())
while n != 0:
    s = int(input())
    if 0 < s < 4 and n >= s:
        n -= s
    print(n)
