"""


В магазине акция: скидка 5% на товары, цена которых превышает 1000 рублей. Напишите программу, отчасти имитирующую
работу кассового аппарата: вводятся цены покупаемых товаров, нужно вывести общую стоимость товаров с учётом скидки.
Формат ввода

Несколько действительных чисел — цены на товары. Каждое число записано в отдельной строке.
Последнее число — отрицательное — сигнал остановки.
Формат вывода

Одно действительное число — общая стоимость товаров с учётом скидки.

"""


skidochka = float(input())
ggwp = 0
while skidochka >= 0:
    if skidochka > 1000:
        ggwp += skidochka * 0.95
    else:
        ggwp += skidochka
    skidochka = float(input())
print(ggwp)
