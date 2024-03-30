"""
Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
"""


def month_name(a, lang):
    if lang == "ru":
        if a == 1:
            return "январь"
        elif a == 2:
            return "февраль"
        elif a == 3:
            return "март"
        elif a == 4:
            return "апрель"
        elif a == 5:
            return "май"
        elif a == 6:
            return "июнь"
        elif a == 7:
            return "июль"
        elif a == 8:
            return "август"
        elif a == 9:
            return "сентябрь"
        elif a == 10:
            return "октябрь"
        elif a == 11:
            return "ноябрь"
        elif a == 12:
            return "декабрь"
    elif lang == "en":
        if a == 1:
            return "January"
        elif a == 2:
            return "February"
        elif a == 3:
            return "March"
        elif a == 4:
            return "April"
        elif a == 5:
            return "May"
        elif a == 6:
            return "June"
        elif a == 7:
            return "July"
        elif a == 8:
            return "August"
        elif a == 9:
            return "September"
        elif a == 10:
            return "October"
        elif a == 11:
            return "November"
        elif a == 12:
            return "December"
