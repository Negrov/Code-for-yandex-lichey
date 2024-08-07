"""


Напишите два класса: LeftParagraph и RightParagraph для печати абзаца с выравниванием по левому и правому краю.

При инициализации экземпляры обоих классов должны принимать целое число — ширину поля вывода. В обоих классах нужно
реализовать метод add_word для добавления слова в абзац и метод end, выводящий полученный абзац на печать и начинающий
формирование нового.

Гарантируется, что длина любого слова меньше ширины поля вывода.

    Формат ввода

Каждый тест представляет собой код, в котором будут использоваться ваши классы.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашими классами, а его вывод сравнивается с правильным решением.

"""


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
