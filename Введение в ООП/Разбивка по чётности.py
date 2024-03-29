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
