"""


Вася решил познать азы ASCII-живописи и, как все начинающие художники, начал с рисования простых фигур.
Помогите Васе написать программу построения прямоугольника n х m, состоящего из символов symb.
Фигура должна быть пустой, а не заполненной. То есть она должна состоять только из контура.
Формат ввода

Два числа, каждое в отдельной строке — высота и ширина прямоугольника.
На третьей строке символ, используемый для рисования контуров.

"""


stolb = int(input())
line = int(input())
simb = input()
print(simb * line)
for i in range(stolb - 2):
    print(f'{simb}{" " * (line - 2)}{simb}')
print(simb * line)
