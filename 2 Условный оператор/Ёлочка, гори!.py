"""
Напишите программу, которая считывает три строки. Если эти три строки – «раз», «два» и «три», то программа выводит
«ГОРИ», если нет, то «НЕ ГОРИ».
"""


one, two, three = input(), input(), input()
if one == "раз" and two == "два" and three == "три":
    print("ГОРИ")
else:
    print("НЕ ГОРИ")
