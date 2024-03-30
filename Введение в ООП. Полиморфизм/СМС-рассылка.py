"""


Для создания смс-рассылки напишите классы Person и Company, а также функцию send_sms.
Объект класса Person при инициализации принимает значения имени, отчества и фамилии человека, а также словарь с номерами
его телефонов.

Класс должен содержать следующие методы:

    get_phone() – возвращает телефон из словаря по ключу 'private' или None, если такого телефона нет,
    get_name() – возвращает фамилию, имя и отчество человека через пробел,
    get_work_phone() – возвращает телефон из словаря по ключу 'work' или None, если такого телефона нет,
    get_sms_text() – возвращает текст «Уважаемый <имя> <отчество>! Примите участие в нашем беспроигрышном конкурсе для
    физических лиц».

Объект класса Company при инициализации принимает название компании, тип компании, словарь с её телефонами, а также
неограниченное количество работников компании (объектов класса Person).

Класс должен содержать следующие методы:

    get_phone() – возвращает телефон из словаря по ключу 'contact', если его нет, то телефон первого работника, у
    которого есть телефон по ключу 'work', или None, если таких работников не найдётся,
    get_name() – возвращает название компании,
    get_sms_text() – возвращает текст «Для компании <название компании> есть супер предложение! Примите участие в нашем
    беспроигрышном конкурсе для <тип компании>».

Функция send_sms должна принимать неограниченное количество объектов класса Person или Company и в случае, если найден
номер для отправки (с помощью метода get_phone()), выводить сообщение «Отправлено СМС на номер <номер> с текстом:
<Текст СМС>», иначе – текст «Не удалось отправить сообщение абоненту: <ФИО человека или название компании>».

"""


class Person:

    def __init__(self, name, fathername, lastname, numbers: dict):
        self.name = name
        self.fathername = fathername
        self.lastname = lastname
        self.numbers = numbers

    def get_phone(self):
        try:
            return self.numbers['private']
        except KeyError:
            return None

    def get_name(self) -> str:
        return f'{self.lastname} {self.name} {self.fathername}'

    def get_work_phone(self):
        try:
            return self.numbers['work']
        except KeyError:
            return None

    def get_sms_text(self):
        return (f'Уважаемый {self.name} {self.fathername}! Примите участие в нашем беспроигрышном конкурсе '
                f'для физических лиц')


class Company:

    def __init__(self, name, type_c, number: dict, *people):
        self.name = name
        self.type_c = type_c
        self.number = number
        self.people = people

    def get_phone(self):

        try:
            return self.number["contact"] if self.number["contact"] else None

        except KeyError:

            for person in self.people:

                if person.get_work_phone():
                    return person.get_work_phone()

            return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return (f'Для компании {self.name} есть супер предложение! Примите участие в нашем'
                f' беспроигрышном конкурсе для {self.type_c}')


def send_sms(*args):
    for user in args:

        if user.get_phone() is not None:
            print(f'Отправлено СМС на номер {user.get_phone()} с текстом: {user.get_sms_text()}')

        else:
            print(f'Не удалось отправить сообщение абоненту: {user.get_name()}')

