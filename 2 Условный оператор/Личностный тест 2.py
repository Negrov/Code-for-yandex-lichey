"""


Напишите программу-тест, которая по некоторым простым вопросам выдаёт «строго индивидуальный» анализ личностных качеств.
Задайте пользователю два-четыре вопроса с тремя-пятью вариантами ответа (например, «Какое ваше любимое время года?») и
считайте его ответы.

Если пользователь при ответе на любой вопрос (в том числе и первый) дал не предусмотренный вами вариант ответа, то надо
сообщить ему об ошибке и сразу же завершить работу.

Если же он дал предусмотренный ответ на каждый из вопросов, выдаём пользователю результат (например, «Вы обладаете
незаурядным умом.»), причём должно быть не менее пяти разных вариантов результата.

Обратите внимание, что программа должна задавать следующий вопрос только при получении корректного ответа на предыдущий.
Примечания

Данная задача дополнительно проверяется преподавателем.

"""


first_vpr = input("Ты не натурал?\n")
if (first_vpr == "Да" or first_vpr == "Нет" or first_vpr == "Хз" or first_vpr == "Может быть"
        or first_vpr == "Конечно нет"):
    second_vpr = input("Любишь шоколад?\n")
    if (second_vpr == "Да" or second_vpr == "Нет" or second_vpr == "Хз" or second_vpr == "Обожаю"
            or second_vpr == "Только чёрный"):
        if first_vpr == "Да" and second_vpr == "Да":
            print("Нууу, по тебе понятно.")
        elif first_vpr == "Да" and second_vpr == "Нет":
            print("Нууу, по тебе понятно, ещё и шоколад не любищь.")
        elif first_vpr == "Да" and second_vpr == "Хз":
            print("Ну просто фу.")
        elif first_vpr == "Да" and second_vpr == "Обожаю":
            print("Много шоколада не ешь, попа слипнится.")
        elif first_vpr == "Да" and second_vpr == "Только чёрный":
            print("В двойне фуу.")
        elif first_vpr == "Нет" and second_vpr == "Да":
            print("Попа слипнится")
        elif first_vpr == "Нет" and second_vpr == "Нет":
            print("Поддерживаю")
        elif first_vpr == "Нет" and second_vpr == "Хз":
            print("Неопределённость какая-то")
        elif first_vpr == "Нет" and second_vpr == "Обожаю":
            print("Нормально")
        elif first_vpr == "Нет" and second_vpr == "Только чёрный":
            print("Как-то странно.")
        elif first_vpr == "Хз" and second_vpr == "Да":
            print("Ты прав.")
        elif first_vpr == "Хз" and second_vpr == "Нет":
            print("Шоколад вкусныйю")
        elif first_vpr == "Хз" and second_vpr == "Хз":
            print("Неопределился пока,да?")
        elif first_vpr == "Хз" and second_vpr == "Обожаю":
            print("Я тоже люблю шоколад.")
        elif first_vpr == "Хз" and second_vpr == "Только чёрный":
            print("Сам чёрный.")
        elif first_vpr == "Может быть" and second_vpr == "Да":
            print("Какая-то полу неопределённость.")
        elif first_vpr == "Может быть" and second_vpr == "Нет":
            print("Ты странненький")
        elif first_vpr == "Может быть" and second_vpr == "Хз":
            print("Слишком сильно, ты, неопределён.")
        elif first_vpr == "Может быть" and second_vpr == "Обожаю":
            print("Ну хоть шоколад любишь.")
        elif first_vpr == "Может быть" and second_vpr == "Только чёрный":
            print("А может быть я чёрный.")
        elif first_vpr == "Конечно нет" and second_vpr == "Да":
            print("Вот ты нормальный мужик.")
        elif first_vpr == "Конечно нет" and second_vpr == "Нет":
            print("Ну это норма.")
        elif first_vpr == "Конечно нет" and second_vpr == "Хз":
            print("Ну ты совсем.")
        elif first_vpr == "Конечно нет" and second_vpr == "Обожаю":
            print("Я думаю молочный любишь.")
        elif first_vpr == "Конечно нет" and second_vpr == "Только чёрный":
            print("А я не люблю чёрный.")
    else:
        print("Error")
else:
    print("Error")
