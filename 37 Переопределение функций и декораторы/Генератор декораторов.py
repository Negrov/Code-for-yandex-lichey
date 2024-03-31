"""
Напишите генератор декораторов check_password, т. е. функцию, которая возвращает декоратор.

Генератор декораторов принимает в качестве параметра пароль, и получившийся декоратор должен закрыть функцию этим
паролем.

Декоратор будет применяться следующим образом:
@check_password(’password’)
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    # ...

Т.е при определении функции сначала вызывается функция check_password() c аргументом "password", получается декоратор,
затем уже этот получившийся декоратор применяется к функции.
"""


def generate_decators(passwd):
    def decorator(password, function):

        if password == passwd:
            return function

        else:
            print("Нет доступа")
            return None

    return decorator
