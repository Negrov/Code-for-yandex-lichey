"""
Напишите функцию squared(a, b, k), которая выводит на экран таблицу квадратов для чисел от a до b, при этом не нужно
выводить квадраты кратные k. Если такое число встречается, его нужно пропустить, вывод переходит к следующему числу.

Строки формируются так. Берем исходное число и возводим в квадрат все числа, от него и до числа, в котором последняя
цифра на 1 меньше, чем в исходном. Затем переходим на следующую строку. В ней нужно будет возводить в квадрат число, в
котором десятков на 1 больше, чем в исходном, а единиц столько же. Например, если надо начать с 14, то заканчиваем
строку на 23, возведенным в квадрат. А следующая строка начнется с квадрата числа 24. Если, конечно, квадраты этих
чисел не кратны k.

Для каждого числа при выводе отводится 4 символа и один символ пробела разделяет столбцы.
"""


def squared(mini, maxi, delit):
    ishod = mini
    for i in range(maxi - mini + 1):
        if (mini + i) ** 2 % delit > 0:
            print(f"{(mini + i) ** 2:<4}", end=" ")
        if ishod % 10 - 1 == (mini + i) % 10:
            print()
            ishod = mini + i + 1
