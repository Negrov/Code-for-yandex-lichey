"""
Почему столько внимания уделяется таблице умножения? Других арифметических операций не бывает, что ли?

Выведите таблицу деления заданных размеров.
Формат ввода
На первой строке вводится число колонок в таблице.

На второй строке вводится число строк в таблице.
Формат вывода
Выводится указанное число строк. В каждой строке выводятся разделённые символами пустого пространства частные: номер
колонки, делённый на номер строки. Нумерация колонок и строк начинается с 1.
"""


stolb = int(input())
string = int(input())
for i in range(1, string + 1):
    for j in range(1, stolb + 1):
        print(j / i, end=" ")
    print()
