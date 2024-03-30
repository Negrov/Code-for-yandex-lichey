"""


Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом отдельно чётные и нечётные. Числа
добавляются в объект с помощью метода add_number. Методы even и odd должны возвращать списки чётных и нечётных чисел
соответственно. Числа в списке должны идти в том же порядке, что и при добавлении в объект.

Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс. Файл c решением не обязательно называть
solution.py, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с
правильным решением.

"""


class OddEvenSeparator:

    def __init__(self):
        self.od = list()
        self.eve = list()

    def add_number(self, num: int) -> None:
        if num % 2 == 0:
            self.eve.append(num)

        else:
            self.od.append(num)

        return

    def even(self) -> list:
        return self.eve

    def odd(self) -> list:
        return self.od
