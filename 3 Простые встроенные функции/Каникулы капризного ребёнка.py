"""


Непросто приходится родителям капризной девочки Жени. Прошлым летом в июле она побывала в Туле, а в августе — в Пензе, и
ей очень понравилось. Поэтому этим летом она снова хочет съездить в два различных города. При этом Женя хочет снова
побывать в июле в Туле или в августе в Пензе, но не то и другое одновременно — повторять прошлогодний маршрут полностью
ей будет скучно. Определите, подходит ли предлагаемый маршрут под требования Жени.
Формат ввода

Вводятся две строки — названия городов, в которые родители собираются отправиться с Женей в июле и в августе.
Формат вывода

Выводится «ДА», если предложенная последовательность городов удовлетворяет требованиям Жени, и «НЕТ», если не
удовлетворяет.

"""


gorod = input()
gorodx = input()
gorodok = "Тула"
gorodokx = "Пенза"
if gorod != gorodx and (gorod == gorodok and gorodx != gorodokx or gorodx == gorodokx and gorod != gorodok):
    print("ДА")
else:
    print("НЕТ")
