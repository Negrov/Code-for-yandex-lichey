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
