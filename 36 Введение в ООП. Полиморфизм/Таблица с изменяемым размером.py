"""


Реализуйте класс Table, который хранит целые числа в двумерной таблице. При инициализации Table(rows, cols) экземпляру
передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.

table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col. Если ячейка с индексами row и col не
лежит внутри таблицы, нужно вернуть None.

table.set_value(row, col, value) — записать число в ячейку строки row, столбца col. Гарантируется, что в тестах будет в
запись только в ячейки внутри таблицы.

table.n_rows() — вернуть число строк в таблице

table.n_cols() — вернуть число столбцов в таблице

table.delete_row(row) — удалить строку с номером row

table.delete_col(col) — удалить колонку с номером col

table.add_row(row) — добавить в таблицу новую строку с индексом row.
Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.

table.add_col(col) — добавить в таблицу новую колонку с индексом col.
Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваш класс.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

"""


class Table(object):

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.table[row][col] if (0 <= row < self.rows and 0 <= col < self.cols) else None

    def set_value(self, row, col, value) -> None:
        self.table[row][col] = value
        return

    def n_rows(self) -> int:
        return self.rows

    def n_cols(self) -> int:
        return self.cols

    def delete_row(self, row) -> None:
        self.table.pop(row)
        self.rows -= 1
        return

    def delete_col(self, col) -> None:

        for row in range(self.rows):
            self.table[row].pop(col)

        self.cols -= 1
        return

    def add_row(self, row) -> None:
        self.table.insert(row, [0 for _ in range(self.cols)])
        self.rows += 1
        return

    def add_col(self, col) -> None:
        for row in range(self.rows):
            self.table[row].insert(col, 0)

        self.cols += 1
        return
