class Selector:

    def __init__(self, values):
        self.values = values.copy()

    def get_odds(self) -> list:
        return [i for i in self.values if i % 2 == 1]

    def get_evens(self) -> list:
        return [i for i in self.values if i % 2 == 0]
