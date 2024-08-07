"""
Вдоль аллеи растут деревья различной высоты. Их высаживали на расстояниях целого числа метров от начала аллеи, но
высаживали разреженно, то есть не на каждом метре высажено по дереву. С одного из концов аллеи светит солнце так, что
деревья отбрасывают тени вдоль аллеи. Ваша задача – узнать, может ли вампир с аллергией на солнечный свет безбоязненно
пройти аллею. Впрочем, аллергия у вампира несильная и суммарно меньше 10 метров прогулки под солнечными лучами он
переносит спокойно, а длины меньше метра в расчет вовсе не идут.

Для того, чтобы выяснить, безопасна ли аллея, вам придется сначала заполнить список, в котором отмечены места света и
тени, а затем посчитать число метровых отметок, которые не прикрыты тенью.
Длина тени k на метр высоты дерева может меняться в зависимости от времени суток, поэтому мы передаем ее как аргумент
функции. Знак k обозначает, в какую сторону Солнце светит. Положительный k означает, что светит от начала к концу аллеи,
отрицательный – в обратную сторону. При k=0 дерево закрывает тенью только то место, на котором оно растёт.

В качестве исходных данных вы будете работать со списком, в котором указана рассадка деревьев через каждый метр аллеи.
Нулевой элемент списка отвечает началу аллеи, первый – расстоянию 1 метр от начала аллеи и т. д. Элементы списка –
высоты деревьев в метрах. Участкам аллеи, на которых деревьев нет в списке сопоставлены нули. Для простоты считать, что
высоты деревьев – целые, коэффициент k – тоже.
Обратите внимание: дерево высоты h может покрыть до kh+1 метровых отметок (начало тени и конец считаются затенёнными).
Часть тени, выступающую за границу аллеи, не учитывайте. См. пример.

Для решения этой задачи напишите три функции:

    Функция make_shades(alley, k) должна вернуть список, в котором булевыми значениями отмечено, покрывает ли тень
    соответствующую метровую отметку.
    Функция calculate_sunny_length(shades) должна получить список покрытия аллеи тенями и вернуть число непокрытых
    тенью метровых отметок
    Функция main() запрашивает у пользователя коэффициент k

и список высот деревьев вдоль аллеи в строку. В ответ печатает на экране “Обгорел”, если вампиру пришлось пройти 10 или
больше метров под солнечным светом (вернее, 10 метровых отметок). Если вампиру пришлось пройти меньше 10 метров под
Солнцем, напечатайте “Тени достаточно”.
"""


def make_shades(alley, k):
    mass = []
    obs = 0
    k2 = k
    if k == -1:
        alley = list(reversed(alley))
        k2 = 1
    if k2 != 0:
        for h in alley:
            if k2 * h > 0 or obs > 0:
                mass.append(True)
                obs -= 1
            else:
                mass.append(False)
            if h >= obs and h > 0:
                obs += k2 * h + 1
    else:
        for h in alley:
            if h > 0:
                mass.append(True)
            else:
                mass.append(False)
    if k == -1:
        return list(reversed(mass))
    else:
        return mass


def calculate_sunny_length(shades):
    return len(list(filter(lambda x: not x, shades)))


def main():
    k = int(input())
    list_h = [int(i) for i in input().split()]
    if calculate_sunny_length(make_shades(list_h, k)) >= 10:
        print("Обгорел")
    else:
        print("Тени достаточно")
