"""
Напишите программу, которая считывает две строки и выводит «ВЕРНО», если в каждой из них записано или слово только да,
или только слово нет (в любой комбинации). Если это не так, выведите «НЕВЕРНО».
"""


exe = input()
text = input()
if (("да " in exe or "нет " in exe or " да" in exe or " нет" in exe or "да" == exe or "нет" == exe)
        and ("да " in text or "нет " in text or " да" in text or " нет" in text or "да" == text or "нет" == text)):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
    