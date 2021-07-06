# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_divide(arg_1, arg_2):
    """
    Divides arg_1 by arg_2.
    If arg_2 is zero returns None.
    """
    if arg_2 == 0:
        return None
    else:
        return arg_1 / arg_2


print(my_divide(3, 2))
print(my_divide(3, 0))
