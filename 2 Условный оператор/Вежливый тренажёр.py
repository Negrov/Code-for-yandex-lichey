"""


Вася заметил, что при наборе текста часто совершает ошибки из-за невнимательности: пропускает букву, заменяет на другую
или дублирует. Он решил, что надо попрактиковаться во вводе текста, а заодно и предложить друзьям такую возможность!

Напишите программу, которая сначала просит ввести имя, а затем текст, который нужно повторить с точностью до регистра и
знаков препинания.

Назовите себя, пожалуйста!

{Пользовательский ввод}

Введите текст.

{Пользовательский ввод}

Повторите текст.

{Пользовательский ввод}

Если текст совпал с повторением, программа выводит обращение по имени и сообщение:

{Имя}, введено верно!

Если не совпал:

{Имя}, пока не получилось, попробуйте снова!

"""

name = input("Назовите себя, пожалуйста!\n")
text = input("Введите текст.\n")
povtor = input("Повторите текст.\n")
if text == povtor:
    print(name + ", введено верно!")
else:
    print(name + ", пока не получилось, попробуйте снова!")
