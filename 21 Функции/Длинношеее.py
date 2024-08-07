"""


Напишите функцию print_long_words(text), которая будет искать в переданной строке слова с четырьмя и более слогами
(гласными буквами). Строка передается параметром функции. Словом следует считать набор букв, ограниченный любыми
символами, не являющимися буквами (либо началом/концом строки).

Найденные слова должны быть выведены на экран в порядке, в котором они встретились. Каждое слово должно идти на своей
строке и печататься маленькими буквами.

В русском языке гласными являются буквы: а, о, э, и, у, ы, е, ё, ю, я. В английском: a, e, i, o, u, y.

Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.

"""


def print_long_words(text):
    text = text.lower()
    for i in text:
        if i not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
            text = text.replace(i, ' ')
    text_copy = text.split()
    for word in text_copy:
        count = 0
        for litter in word:
            count += 1 if litter in 'аоэиуыеёюяaeiouy' else 0
        if count >= 4:
            print(word)
