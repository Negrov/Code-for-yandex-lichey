"""


Во многих задачах, связанных с компьютерами, особенно близких к аппаратной части, важную роль играют числа, являющиеся
степенями двойки: 1, 2, 4, 8 и так далее. Напишите программу, которая проверяет, является ли введённое натуральное число
степенью двойки. Если да, то выводится сама эта степень; если нет, выводится «НЕТ».
Формат ввода

Одно целое число.
Формат вывода

Одно целое число (показатель степени) или строка «НЕТ».

"""


num = int(input())
stepen = 0
while num % 2 == 0:
    num /= 2
    stepen += 1
if num == 1:
    print(stepen)
else:
    print("НЕТ")
