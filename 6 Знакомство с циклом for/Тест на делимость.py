"""


Напишите ещё одну программу для самоконтроля навыков устного счёта. Для каждого числа i от 0 до 16 (включительно)
вводится с клавиатуры некоторое натуральное число d. Ваша задача — проверить, делится ли i на d, и вывести «ДА» или
«НЕТ» в зависимости от этого. (То есть, делится ли 0 на первое введенное число, 1 - на второе введенное число и т.д.)
Например, на последней строке вывода будет «ДА», только если на последней строке ввода было 1, 2, 4, 8 или 16.

Если ввод и вывод производится в одной и той же консоли, то строки ввода и вывода будут перемешаны. Автоматической
проверке это не помешает.
Формат ввода

17 натуральных чисел.
Формат вывода

Для каждого из введенных чисел сообщение «ДА» или «НЕТ» на отдельной строчке.

"""


for el in range(17):
    if el % int(input()):
        print("НЕТ")
    else:
        print("ДА")
