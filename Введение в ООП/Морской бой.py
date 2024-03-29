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


sm = SeaMap()

sm.shoot(0, 0, 'hit')
sm.shoot(0, 1, 'sink')

sm.shoot(9, 8, 'hit')
sm.shoot(9, 9, 'sink')

sm.shoot(2, 3, 'sink')

sm.shoot(5, 6, 'miss')
sm.shoot(7, 8, 'miss')
sm.shoot(1, 7, 'miss')

sm.shoot(1, 7, 'miss')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
