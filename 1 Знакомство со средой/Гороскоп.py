"""


У нас есть бизнес-план!

Пункт первый: надо написать программу-гороскоп, которая по некоторым простым вопросам выдаёт строго индивидуальный
анализ личностных качеств. Мы будем делать это по передовым астрологическим методикам. Напишите программу, которая
считывает с клавиатуры последовательно: имя, фамилию, любимое животное, знак зодиака.

После этого программа выводит:

Индивидуальный гороскоп для пользователя [имя] [фамилия]
Кем вы были в прошлой жизни: [любимое животное]
Ваш знак зодиака - [знак зодиака] , поэтому вы - тонко чувствующая натура.

Уточнение: слова про тонко чувствующую натуру выводятся абсолютно всегда, независимо от того, что именно вводил
пользователь (это пародия на процесс составления «реального» гороскопа). В один и тот же фиксированный текст
подставляются те слова, которые вводил пользователь.

Пробел перед запятой по правилам, конечно, не ставится, но здесь пусть стоит.

"""


name = input()
surname = input()
tegr = input()
znak = input()
print("Индивидуальный гороскоп для пользователя", name, surname)
print("Кем вы были в прошлой жизни:", tegr)
print("Ваш знак зодиака -", znak, ", поэтому вы - тонко чувствующая натура.")
