"""


Маша рассказала Толе, что считает трехзначное число красивым, если в нём полусумма максимальной и минимальной по
значению цифр равна оставшейся цифре числа. Помогите Толе впечатлить Машу – написать программу, которая будет определять
красивые числа. Выведите для красивого числа фразу "Вы ввели красивое число", а для остальных - "Жаль, вы ввели обычное
число".
Формат ввода

Строка, содержащая трехзначное число.
Формат вывода

Вердикт программы-строка.

"""


beauty_num = int(input())
one = beauty_num // 100
two = beauty_num // 10 % 10
three = beauty_num % 10
summa = one + two + three
max_one = max(one, two, three)
min_three = min(one, two, three)
summa = summa - max_one - min_three
if (max_one + min_three) / 2 == summa:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
    