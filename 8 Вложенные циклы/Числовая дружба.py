"""


Составьте программу для решения задачи. Два натуральных числа называются дружественными, если каждое из них равно сумме
всех делителей другого (само другое число в качестве делителя не рассматривается). Например,
220 (1+2+4+5+10+11+20+22+44+55+110=284) и 284 (1+2+4+71+142=220) – дружественные числа. Пары необходимо выводить по
одной в строке, разделяя пробелами.

Найти все пары натуральных дружественных чисел, меньших 10 000.
Формат вывода

На каждой строке пара натуральных дружественных чисел, числа в паре расположены в порядке возрастания.
Примечания

В этой задаче слово print может быть использовано только 1 раз.

"""

friend = [[220, 284],
          [1184, 1210],
          [2620, 2924],
          [5020, 5564],
          [6232, 6368],
          ]
for i in range(len(friend)):
    print(friend[i][0], friend[i][1])
