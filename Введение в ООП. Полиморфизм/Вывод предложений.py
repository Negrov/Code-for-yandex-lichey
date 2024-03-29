class Paragraph:

    def __init__(self, length):
        self.length = length
        self.text = list()


class LeftParagraph(Paragraph):

    def add_word(self, word) -> None:

        if not len(self.text):
            self.text.append(word)

        else:

            if len(self.text[-1]) + len(word) < self.length:
                self.text[-1] += ' ' + word

            else:
                self.text.append(word)

        return

    def end(self) -> None:
        print(*self.text, sep='\n')
        self.text.clear()
        return


class RightParagraph(Paragraph):

    def add_word(self, word):

        if not len(self.text):
            self.text.append(word)

        else:

            if len(self.text[-1]) + len(word) < self.length:
                self.text[-1] += ' ' + word

            else:
                self.text.append(word)

        return

    def end(self) -> None:

        for line in self.text:
            print(f"{line:>{self.length}}")

        self.text.clear()
        return
