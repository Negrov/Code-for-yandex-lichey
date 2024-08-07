"""


Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее арифметическое
последовательности целых чисел.

Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число, которое будет
учтено при вычислении финального результата методом result. Для экземпляров MinStat и MaxStat result должен возвращать
целое число, для AverageStat — число типа float (это число будет сравниваться с правильным ответом до седьмой значащей
цифры).

Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен
возвращать None.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваши классы.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашими классами, а его вывод сравнивается с правильным решением.

"""


class MinStat(object):
    def __init__(self):
        self.arr = []

    def add_number(self, x) -> None:
        self.arr.append(x)
        return

    def result(self) -> int:
        return min(self.arr) if self.arr else None


class MaxStat(MinStat):

    def result(self) -> int:
        return max(self.arr) if self.arr else None


class AverageStat(MinStat):

    def result(self) -> float:
        return sum(self.arr) / len(self.arr) if self.arr else None
