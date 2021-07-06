# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def my_func():
    """
    Prints the sum of digits divided by space character
    """
    result = 0
    while True:
        end = False
        input_list = input('Input digit string divided by space (for end type q) - ').split(sep=' ')
        try:
            input_list.remove('q')
            end = True
        except ValueError:
            end = False
        finally:
            input_list = list(map(int, input_list))
            result += sum(input_list)
            print(f'Result: {result}')
        if end:
            break


my_func()

