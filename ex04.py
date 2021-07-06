# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(arg_1, arg_2):
    """    
    :param arg_1: Base
    :param arg_2: Power
    :return: Exponentiation arg_1 by arg_2
    """
    return arg_1 ** arg_2


def my_func2(arg_1, arg_2):
    """
    :param arg_1: Base
    :param arg_2: Power
    :return: Exponentiation arg_1 by arg_2
    """
    result = 1
    for i in range(abs(arg_2)):
        result *= arg_1
    return 1 / result


print(my_func1(2, -4))
print(my_func2(2, -4))

