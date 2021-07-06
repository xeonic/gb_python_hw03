# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_max_searching(arg_1, arg_2, arg_3):
    """
    Returns the two biggest elements sum
    :param arg_1: Element 1
    :param arg_2: Element 2
    :param arg_3: Element 3
    """
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    return my_list[1] + my_list[2]


print(my_max_searching(1, 2.5, -20))
print(my_max_searching('q', 'qw', 'qwe'))
