"""


В танце очень важно чувствовать ритм музыки. Напишите программу, которая проверяет, правильно ли ученик отсчитывает: раз, два, три, четыре, раз, два, три, четыре... При этом считается, что у учителя есть некоторый ограниченный запас терпения, и после определённого числа ошибок он заканчивает занятие.
Формат ввода

На первой строке вводится натуральное число n — запас терпения учителя.

Далее следуют строки с отсчётами.
Формат вывода

Пока в вводе повторяются по очереди строки «раз», «два», «три», «четыре», программа не выводит ничего. Как только выводится что-то иное, чем ожидалось, программа выводит: «Правильных отсчётов было <количество правильных отсчётов>, но теперь вы ошиблись.» (Количество правильных отсчётов после этого считается заново, и сами отсчёты снова должны начинаться с «раз».) Если это произошло в n-й раз, выводится «На сегодня хватит.», и дальнейший ввод игнорируется.

"""


count = 0
n = int(input())
while n:
    if input() == "раз":
        count += 1
        if input() == "два":
            count += 1
            if input() == "три":
                count += 1
                if input() == "четыре":
                    count += 1
                    continue
    print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
    count = 0
    n -= 1
print('На сегодня хватит.')
