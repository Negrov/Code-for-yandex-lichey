"""


Аня и Наташа играют в города. Они очень любят эту игру, знают много городов и к концу игры забывают, какие уже называли.
На вас возложена почётная задача вести запись игры и напоминать девочкам, если какой-то город уже был назван.
Формат ввода

В первой строке записано число названных городов N. Затем идут N строк с названиями городов и ещё одна строка с новым
только что названым городом.
Формат вывода

Слово OK, если такого города ещё не было названо, и TRY ANOTHER, если город уже был назван.

"""

lim = int(input())
city = set()

for i in range(lim):
    city.add(str(input()))

pizda = str(input())
if pizda not in city:

    print('OK')

else:

    print("TRY ANOTHER")
