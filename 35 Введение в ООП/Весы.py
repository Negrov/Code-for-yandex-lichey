"""


Напишите класс Balance для описания весов с двумя чашами. На левую и правую чашу объекта будут добавляться грузы с
различным весом, ваша задача определить положение чаш.

Метод add_right принимает целое число — вес, положенный на правую чашу весов, add_left — на левую чашу. Метод result
должен возвращать символ =, если вес на чашах одинаковый, R — если перевесила правая, L — если перевесила левая.

Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс. Файл c решением не обязательно называть
solution.py, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с
правильным решением.

"""


class Balance:

    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, drop) -> None:
        self.right += drop
        return

    def add_left(self, drop) -> None:
        self.left += drop
        return

    def result(self) -> str:
        if self.left == self.right:
            return '='

        elif self.left > self.right:
            return 'L'

        else:
            return 'R'
