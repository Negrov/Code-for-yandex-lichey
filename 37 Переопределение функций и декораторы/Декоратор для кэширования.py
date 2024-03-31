"""
Напишите декоратор cached, который будет кэшировать результат вызова функции.

Пример того, как можно будет использовать ваш декоратор:
@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
"""

from hashlib import sha256


def cached(func):

    def wrapper():
        result = func()
        return sha256(result)

    return wrapper


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
