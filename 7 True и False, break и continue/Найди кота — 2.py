"""


Напишите программу, которая находит кота.

Пользователь вводит строки до тех пор, пока он не введёт «СТОП». Программа выводит номер строки, на которой впервые был
упомянут кот (в том же смысле, что и в предыдущей задаче), или -1 (минус один), если кот не был упомянут.
Формат ввода

Несколько строк.
Сигнал остановки — строка «СТОП».
Формат вывода

Одно число — номер первой строчки, в которой появился кот, или -1, если кота нет.

"""


count = 0
que = -1
string: str = "Аf"
flag = True
while string != "СТОП":
    if "кот" in string.lower() and flag:
        que = count
        flag = False
    string = input()
    count += 1
print(que)
