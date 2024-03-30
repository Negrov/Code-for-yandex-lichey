"""


Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:

    new_game() – для создания новой игры;
    get_field() – для получения поля (список списков);
    check_field() – для проверки, есть ли победитель, который возвращает X, если победил первый игрок, 0, если второй,
    D, если ничья и None, если можно продолжать игру;
    make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col, если это
    возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков, «Победил
    игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после данного хода
    неопределён.

Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке уже стоит
крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или закончились ячейки для ходов.

При создании объекта класса должна создаваться новая игра.
Аргументы row и col метода make_move могут принимать значения от 1 до 3.

"""


class TicTacToeBoard:

    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.step = 1
        self.finish = False

    def new_game(self) -> None:
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.step = 1
        self.finish = False
        return

    def get_field(self) -> list[list[str]]:
        return self.board

    def check_field(self) -> str:

        flag_x = False
        flag_o = False

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    flag_x = True
                elif self.board[i][0] == '0':
                    flag_o = True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    flag_x = True
                elif self.board[0][i] == '0':
                    flag_o = True

        if (self.board[0][0] == self.board[1][1] == self.board[2][2]
                or self.board[2][0] == self.board[1][1] == self.board[0][2]):
            if self.board[1][1] == 'X':
                flag_x = True
            elif self.board[1][1] == '0':
                flag_o = True

        if flag_x:
            return 'X'
        if flag_o:
            return '0'

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return "None"  # Если не работает уберите ковычки

        return 'D'

    def make_move(self, row, col) -> str:

        if self.finish:
            return 'Игра уже завершена'

        if self.step == 1:
            step = 'X'
        else:
            step = '0'

        if self.board[row - 1][col - 1] == '-':
            self.board[row - 1][col - 1] = step

        else:
            return f'Клетка {row}, {col} уже занята'

        result = self.check_field()
        self.step *= -1

        if result == 'X' or result == '0':
            self.finish = True
            return f'Победил игрок {result}'

        elif result == 'D':
            self.finish = True
            return 'Ничья'

        else:
            return 'Продолжаем играть'
