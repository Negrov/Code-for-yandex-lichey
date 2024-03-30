"""


Как известно, когда мы придумываем пароль от аккаунта ВКонтакте, электронной почты или Яндекс.Контеста, к этому паролю
часто предъявляются определённые требования по сложности.

Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь вводит пароль, потом ещё
раз его же, для подтверждения.

    если пароль, который ввёл пользователь (в первый раз) короче 8 символов, программа выводит "Короткий!" и завершает
    свою работу
    если пароль, введённый пользователем в первый раз, достаточно длинный, но в нём содержится сочетание символов "123",
    программа выводит "Простой!"
    если же предыдущие проверки пройдены успешно, но введённый во второй раз пароль не совпадает с первым, программа
    выводит "Различаются."
    если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами)

Формат ввода

Две строки — пароль, введённый пользователем в первый и во второй раз.
Формат вывода

Одна строка — результат проверки паролей.

"""

passwd1 = input()
if len(passwd1) < 8:
    print("Короткий!")
elif "123" not in passwd1:
    passwd2 = input()
    if passwd1 == passwd2:
        print("OK")
    else:
        print("Различаются.")
else:
    print("Простой!")
