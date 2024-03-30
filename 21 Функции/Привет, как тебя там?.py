"""
Напишите функцию who_are_you_and_hello(), которая читает имя пользователя из стандартного ввода, пока он не введет его в
правильном формате, а затем здоровается. Приветствие должно быть в форме: “Привет, {имя}!”. После вывода надо не забыть
перевести курсор на новую строку.

Если пользователь ввёл имя в неправильной форме, функция должна считать его снова. Корректным считается имя, состоящее
из одного слова, в котором нет символов кроме букв, первая буква заглавная, остальные — строчные.

После вывода приветствия функция должна завершить свою работу.

Обратите внимание: в вашей программе должна быть функция who_are_you_and_hello, но она не должна вызываться. Следите за
тем, чтобы имя функции было написано верно.
Формат ввода
who_are_you_and_hello()

C клавиатуры вводится:

Зачем тебе это знать?
Хорошо, записывай
Василий Пупкин
Василий 1
Вася1
Вася!
ВАСЯ
Вася
И тебе привет
Михаил?
Михаил
Формат вывода
Привет, Вася!
Примечания
Данную задачу вы можете решить методами, описанными в уроке по методам списков и строк. Но, к сожалению, в него нельзя
было включить все возможные строковые методы, поэтому для каждого программиста крайне важным является работа с
документацией. Изучите официальную документацию: https://docs.python.org/3/library/stdtypes.html#string-_methods и
найдите метод, позволяющий более эффективно решить поставленную задачу.
"""


def who_are_you_and_hello():
    problem = {'2', '1', '3', '4', '5', '6', '7', '8', '9'}
    strip = "?/,.!@#$%^&*()_+-=./:;<=>?{}[] '"
    problem = set(strip) | problem
    while True:
        if (set(x := input()) - problem) == set(x) and x == x.capitalize():
            print(f'Привет, {x}!')
            break

