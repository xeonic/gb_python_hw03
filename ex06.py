# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(arg_1=''):
    """
    Make the first letter in word upper case
    :param arg_1: Input word
    :return: Word with first letter upper case
    """
    return arg_1.capitalize()


def my_func(arg_1):
    """
    Make the first letter in each word upper case
    :param arg_1: Input string
    :return: Capitalized string
    """
    string_list = str(arg_1).split(' ')
    string_list = list(map(int_func, string_list))
    return ' '.join(string_list)


print(int_func('blablabal'))
print(my_func('qwer rewq qwer tyuugfvd erwrw'))
