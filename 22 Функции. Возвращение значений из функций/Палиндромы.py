"""


Палиндром — это строка (или слово), которая читается одинаково в обоих направлениях, например, «12321» или известный
пример Афанасия Фета «А роза упала на лапу Азора».

Напишите функцию palindrome(s), которая принимает в качества параметра строку и определяет, является ли она палиндромом.
Функция должна возвращать строку «Палиндром» или «Не палиндром» соответственно.

"""


def palindrome(string):
    string = string.lower().strip()
    string = "".join([word for word in string.split(" ")])
    if string == string[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
    