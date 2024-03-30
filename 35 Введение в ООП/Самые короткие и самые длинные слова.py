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
