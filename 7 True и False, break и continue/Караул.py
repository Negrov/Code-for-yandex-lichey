"""


Аборигены Забытых Островов считают числа, кратные 3, несчастливыми, кратные 7 – опасными, а если число кратно и 3 и 7,
то это адская смесь, их надо избегать любыми способами.

Напишите программу, которая встретив число, кратное 3 или 7, сообщает, что оно несчастливое или опасное соответственно,
а кратное и тому и другому – кричит Караул! И завершает работу.
Формат ввода

Вводятся числа, пока не будет введен 0.
Формат вывода

Если число не кратно ни 3, ни 7, оно просто выводится без изменений, если 3 или 7, то выводить свойство числа, если 3 и
7 одновременно, то вывести Караул! и прекратить работу.

"""


num = int(input())
while num != 0:
    if num % 21 == 0:
        print("Караул!")
        break
    elif num % 3 == 0:
        print("несчастливое")
    elif num % 7 == 0:
        print("опасное")
    else:
        print(num)
    num = int(input())
