"""


Как известно, когда мы придумываем пароль от аккаунта ВКонтакте, электронной почты или Яндекс.Контеста, к этому паролю
часто предъявляются определённые требования по сложности.

Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь вводит пароль, потом ещё
раз его же, для подтверждения.

    если пароль, который ввёл пользователь (в первый раз) короче 8 символов, программа выводит "Короткий!" и завершает
    свою работу
    если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа выводит
    "Различаются."
    если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами).

Формат ввода

Две строки — первый и второй пароль, введенные пользователем.
Формат вывода

Одна строка — результат проверки пароля.

"""


pas = input()
if len(pas) > 7:
    pass1 = input()
    if pas == pass1:
        print("OK")
    else:
        print("Различаются.")
else:
    print("Короткий!")
    