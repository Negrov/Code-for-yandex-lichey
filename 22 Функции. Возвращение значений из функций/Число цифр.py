"""
Напишите функцию num_digits(number), вычисляющую и возвращающую число цифр в десятичном натуральном числе.

Пример:
num_digits(1) # => 1
num_digits(157) # => 3
"""


from math import log10


def num_digits(num) -> int:
    return int(log10(num) + 1)
