"""


Вводится 4-х значное число. Нужно разделить его на отдельные цифры и с их помощью записать наименьшее возможное, но тоже
четырехзначное число. В задаче нельзя использовать циклы, строки и списки.
Формат ввода

Четырехзначное число.
Формат вывода

Минимальное число, записанное теми же цифрами.

"""


four = int(input())
f = four // 1_000
o = four // 100 % 10
u = four // 10 % 10
r = four % 10
mini = min(f, o, u, r)
if f != 0 and o != 0 and u != 0 and r != 0:
    if mini == f:
        mini = min(o, u, r)
        if mini == o:
            print(f"{f}{o}{min(u, r)}{max(u, r)}")
        elif mini == u:
            print(f"{f}{u}{min(o, r)}{max(o, r)}")
        else:
            print(f"{f}{r}{min(u, o)}{max(u, o)}")
    elif mini == o:
        mini = min(f, u, r)
        if mini == f:
            print(f"{o}{f}{min(u, r)}{max(u, r)}")
        elif mini == u:
            print(f"{o}{u}{min(f, r)}{max(f, r)}")
        else:
            print(f"{o}{r}{min(u, f)}{max(u, f)}")
    elif mini == u:
        mini = min(o, f, r)
        if mini == o:
            print(f"{u}{o}{min(f, r)}{max(f, r)}")
        elif mini == f:
            print(f"{u}{f}{min(o, r)}{max(o, r)}")
        else:
            print(f"{u}{r}{min(f, o)}{max(f, o)}")
    else:
        mini = min(o, u, f)
        if mini == o:
            print(f"{r}{o}{min(u, f)}{max(u, f)}")
        elif mini == u:
            print(f"{r}{u}{min(o, f)}{max(o, f)}")
        elif mini == f:
            print(f"{r}{f}{min(u, o)}{max(u, o)}")
elif ((f == 0 and o != 0 and u != 0 and r != 0) or (f != 0 and o == 0 and u != 0 and r != 0)
      or (f != 0 and o != 0 and u == 0 and r != 0) or (f != 0 and o != 0 and u != 0 and r == 0)):
    if mini == f:
        mini = min(o, u, r)
        if mini == o:
            print(f"{o}{f}{min(u, r)}{max(u, r)}")
        elif mini == u:
            print(f"{u}{f}{min(o, r)}{max(o, r)}")
        else:
            print(f"{r}{f}{min(u, o)}{max(u, o)}")
    elif mini == o:
        mini = min(f, u, r)
        if mini == f:
            print(f"{f}{o}{min(u, r)}{max(u, r)}")
        elif mini == u:
            print(f"{u}{o}{min(f, r)}{max(f, r)}")
        else:
            print(f"{r}{o}{min(u, f)}{max(u, f)}")
    elif mini == u:
        mini = min(o, f, r)
        if mini == o:
            print(f"{o}{u}{min(f, r)}{max(f, r)}")
        elif mini == f:
            print(f"{f}{u}{min(o, r)}{max(o, r)}")
        else:
            print(f"{r}{u}{min(f, o)}{max(f, o)}")
    else:
        mini = min(o, u, f)
        if mini == o:
            print(f"{o}{r}{min(u, f)}{max(u, f)}")
        elif mini == u:
            print(f"{u}{r}{min(o, f)}{max(o, f)}")
        elif mini == f:
            print(f"{f}{r}{min(u, o)}{max(u, o)}")
elif four % 1000 == 0:
    print(four)
else:
    if mini == f:
        mini = min(o, u, r)
        if mini == o:
            print(f"{min(u, r)}{f}{o}{max(u, r)}")
        elif mini == u:
            print(f"{min(o, r)}{f}{u}{max(o, r)}")
        else:
            print(f"{min(u, o)}{f}{r}{max(u, o)}")
    elif mini == o:
        mini = min(f, u, r)
        if mini == f:
            print(f"{min(u, r)}{o}{f}{max(u, r)}")
        elif mini == u:
            print(f"{min(f, r)}{o}{u}{max(f, r)}")
        else:
            print(f"{min(u, f)}{o}{r}{max(u, f)}")
    elif mini == u:
        mini = min(o, f, r)
        if mini == o:
            print(f"{min(f, r)}{u}{o}{max(f, r)}")
        elif mini == f:
            print(f"{min(o, r)}{u}{f}{max(o, r)}")
        else:
            print(f"{min(f, o)}{u}{r}{max(f, o)}")
    else:
        mini = min(o, u, f)
        if mini == o:
            print(f"{min(u, f)}{r}{o}{max(u, f)}")
        elif mini == u:
            print(f"{min(o, f)}{r}{u}{max(o, f)}")
        elif mini == f:
            print(f"{min(u, o)}{r}{f}{max(u, o)}")
