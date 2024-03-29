class MinMaxWordFinder:
    def __init__(self):
        self.text = []

    def add_sentence(self, add) -> None:

        for i in add.split():
            self.text.append((len(i), i))

        return

    def shortest_words(self) -> list[int]:
        return sorted([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[0]])

    def longest_words(self) -> list[int]:
        return sorted(set([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[-1]]))
