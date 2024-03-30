"""


Реализуйте класс Table, который хранит целые числа в двумерной таблице. При инициализации Table(rows, cols) экземпляру
передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля. Ячейки таблицы инициализируются нулями.

table.get_value(row, col) — прочитать значение из ячейки со строкой row, столбцом col. Если ячейка с индексами row и col
не лежит внутри таблицы, нужно вернуть None.

table.set_value(row, col, value) — записать число в ячейку со строкой row, столбцом col. Гарантируется, что в тестах
будет в запись только в ячейки внутри таблицы.

table.n_rows() — вернуть число строк в таблице.

table.n_cols() — вернуть число столбцов в таблице.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваш класс.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

"""


class Table:

    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col) -> int:

        if row in range(self.rows) and col in range(self.cols):
            return self.table[row][col]

    def set_value(self, row, col, value) -> None:
        self.table[row][col] = value
        return

    def n_rows(self) -> int:
        return self.rows

    def n_cols(self) -> int:
        return self.cols
