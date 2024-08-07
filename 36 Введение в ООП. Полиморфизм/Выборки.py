"""


Напишите класс Selector.
Экземпляр этого класса при инициализации получает список чисел. Вызов метода get_odds возвращает нечётные числа из
первоначального списка, вызов get_evens — чётные.

Числа должны идти в том же порядке, в котором они были в изначальном списке.

    Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

"""


class Selector:

    def __init__(self, values):
        self.values = values.copy()

    def get_odds(self) -> list:
        return [i for i in self.values if i % 2 == 1]

    def get_evens(self) -> list:
        return [i for i in self.values if i % 2 == 0]
