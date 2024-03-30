"""


Напишите класс MinMaxWordFinder. Класс должен уметь анализировать текст и находить в нём слова наименьшей и наибольшей
длины. Текст состоит из предложений, которые добавляются в обработку методом add_sentence. Метод shortest_words
возвращает список самых коротких на данный момент слов, метод longest_words — самых длинных. Слова, возвращаемые
методами shortest_words и longest_words, должны быть отсортированы по алфавиту.

Если одно из самых коротких слов встретилось в исходных предложениях несколько раз, оно должно столько же раз
повториться в списке самых коротких слов. Самые длинные слова наоборот должны входить в список без повторов.

Формат ввода

Каждый тест представляет собой код, в котором будет использоваться ваш класс. Файл c решением не обязательно называть
solution.py, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с
правильным решением.

"""


class BoundingRectangle:

    def __init__(self):
        self.points = list()

    def add_point(self, *point) -> None:
        self.points.append([point[0], point[1]])
        return

    def width(self) -> int:
        x = [i[0] for i in self.points]
        return max(x) - min(x)

    def height(self) -> int:
        y = [i[1] for i in self.points]
        return max(y) - min(y)

    def bottom_y(self) -> int:
        return min([i[1] for i in self.points])

    def top_y(self) -> int:
        return max([i[1] for i in self.points])

    def left_x(self) -> int:
        return min([i[0] for i in self.points])

    def right_x(self) -> int:
        return max([i[0] for i in self.points])
