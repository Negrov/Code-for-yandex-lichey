"""


Дима любит играть в морской бой. К сожалению, он очень рассеян и постоянно неправильно отмечает на карте клетки, по
которым уже стрелял. Напишите класс, который будет строить за Диму карту.

Класс SeaMap должен иметь следующие методы (sm – экземпляр SeaMap):

sm.shoot(row, col, result) — добавить на карту результат выстрела, где
row — индекс ряда карты,
col — индекс вертикальной колонки карты,
result — одна из строк: “miss” (промах), “hit” (попадание), “sink” (потопление корабля).

sm.cell(row, col), который
возвращает ‘.’, если в клетке с координатами row, col может находиться корабль,
возвращает ‘*’, если в клетку уже стреляли или она находится рядом с потопленным кораблём,
возвращает ‘x’ если в клетке было попадание.

Учтите, что не нужно помечать ‘*’ клетки рядом с кораблём, в который попали, но не потопили до конца.

Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс. Файл c решением не обязательно называть
solution.py, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с
правильным решением.

"""


class SeaMap:

    def __init__(self):
        self.board = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, rowi, coli, result) -> None:

        if result == 'miss':
            self.board[rowi][coli] = '*'

        elif result == 'hit':
            self.board[rowi][coli] = 'x'

        elif result == 'sink':

            for i in range(rowi - 1, rowi + 2):

                for j in range(coli - 1, coli + 2):

                    if 0 <= i < 10 and 0 <= j < 10:

                        if self.board[i][j] == '.':
                            self.board[i][j] = '*'

            self.board[rowi][coli] = 'x'

            for j in range(len(self.board)):

                if self.board[rowi][j] == 'x':
                    coli = j

                    for i in range(rowi - 1, rowi + 2):

                        for u in range(coli - 1, coli + 2):

                            if 0 <= i < 10 and 0 <= u < 10:

                                if self.board[i][u] == '.':
                                    self.board[i][u] = '*'

            for v in range(len(self.board)):

                if self.board[v][coli] == 'x':

                    rowi = v

                    for i in range(rowi - 1, rowi + 2):

                        for u in range(coli - 1, coli + 2):

                            if 0 <= i < 10 and 0 <= u < 10:

                                if self.board[i][u] == '.':
                                    self.board[i][u] = '*'
        return

    def cell(self, rowi, coli) -> str:
        return self.board[rowi][coli]
