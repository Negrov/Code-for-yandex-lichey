"""


C клавиатуры вводится натуральное число n > 0, потом n чисел, каждое на новой строке.

Вычислите и напечатайте знакочередующуюся сумму ряда (первое число прибавить, второе вычесть, третье прибавить и т.д.)
Например, для чисел 1,2,3,4 сумма будет следующей: 1 - 2 + 3 - 4 = -2.

"""


summa = 0
a = -1
for el in range(int(input())):
    summa += (a := a * - 1) * int(input())
print(summa)
