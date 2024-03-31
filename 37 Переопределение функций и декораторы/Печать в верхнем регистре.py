"""
Подмените функцию print() так, чтобы она ПЕЧАТАЛА ВЕСЬ ТЕКСТ В ВЕРХНЕМ РЕГИСТРЕ. Реализовывать работу с именованными
аргументами (sep, end, ...) не нужно.
"""


import sys


def print(*args: str):
    sys.stdout.write(" ".join([x.upper() for x in args]))
