"""
Вводится произвольное целое число. Выведите число, составленное из этих же цифр в обратном порядке.
"""


num = (input())
i = 0
number = 0

while i < len(num):

    power1 = 10 ** (i + 1)
    power2 = 10 ** i
    number1 = (int(num) % power1) // (power2)
    number2 = 10 ** (len(num) - 1 - i)
    number3 = number1 * number2
    number = number + number3
    i += 1

print(number)
