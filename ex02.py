# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_input(name, surname, birth, city, email, mobile):
    """
    Generates formatted string from arguments.
    :param name: Persons name.
    :param surname: Persons surname.
    :param birth: Persons birth year.
    :param city: Current city.
    :param email: E-mail.
    :param mobile: Mobile phone number.
    """
    return f'{name} {surname} lives in {city} and was born in {birth}.\nContact email: {email}, phone: {mobile}'


print(my_input(name='Michal', surname='Judachin', city='Liberec', birth=1986, email='xeonic@seznam.cz', mobile='775351848'))
