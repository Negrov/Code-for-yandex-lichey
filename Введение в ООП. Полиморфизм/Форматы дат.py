"""


Форматы записи дат в виде строки в США и Европе отличаются.
В США принят формат мм.дд.гггг, в Европе — дд.мм.гггг, где дд — день (дополняется нулём слева, если число меньше 10), 
мм — месяц (так же дополняется нулём слева), гггг — год.
Например, 10 апреля 2000 года будет записано в американском формате как 04.10.2000, а в европейском — как 10.04.2000.
Все годы в задаче — четырёхзначные.

Реализуйте классы AmericanDate и EuropeanDate. При инициализации они должны принимать год, месяц и число
(именно в этом порядке). Так же должны быть реализованы методы set_year, set_month, set_day для изменения одной из
компонентов даты, и get_year, get_month, get_day для чтения компонентов даты. Метод format должен возвращать строковое
представление (своё для каждого класса).

Гарантируется, что все даты в тестах корректны и существуют в календаре.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваши классы.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашими классами, а его вывод сравнивается с правильным решением.

"""


class AmericanDate:

    def __init__(self, y, m, d):
        self.year = str(y)
        self.month = str(m)
        self.day = str(d)

    def get_year(self) -> str:
        return self.year

    def get_month(self) -> str:
        return self.month

    def get_day(self) -> str:
        return self.day

    def set_year(self, ny) -> str:
        self.year = str(ny)
        return self.year

    def set_month(self, nm) -> str:
        self.month = str(nm)
        return self.month

    def set_day(self, nd) -> str:
        self.day = str(nd)
        return self.day

    def format(self) -> str:

        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'

        elif len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.0{self.get_day()}.{self.get_year()}'

        elif len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.{self.get_day()}.{self.get_year()}'

        elif len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.0{self.get_day()}.{self.get_year()}'


class EuropeanDate:

    def __init__(self, y, m, d):
        self.year = str(y)
        self.month = str(m)
        self.day = str(d)

    def get_year(self) -> str:
        return self.year

    def get_month(self) -> str:
        return self.month

    def get_day(self) -> str:
        return self.day

    def set_year(self, ny) -> str:
        self.year = ny
        return self.year

    def set_month(self, nm) -> str:
        self.month = str(nm)
        return self.month

    def set_day(self, nd) -> str:
        self.day = str(nd)
        return self.day

    def format(self) -> str:

        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_day()}.{self.get_month()}.{self.get_year()}'

        elif len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_day()}.0{self.get_month()}.{self.get_year()}'

        elif len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'{self.get_day()}.0{self.get_month()}.{self.get_year()}'

        elif len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'0{self.get_day()}.{self.get_month()}.{self.get_year()}'
