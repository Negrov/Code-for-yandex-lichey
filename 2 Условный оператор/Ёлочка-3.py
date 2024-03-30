"""
Добавьте в предыдущую программу возможность вместо «раз» ввести «один».
"""


one, two, three = input(), input(), input()
if one == "раз" and two == "два" and three == "три":
    print("ГОРИ")
elif one == "1" and two == "2" and three == "3":
    print("ГОРИ")
elif one == "один" and two == "два" and three == "три":
    print("ГОРИ")
else:
    print("НЕ ГОРИ")
