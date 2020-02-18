def division(div_1, div_2):
    """
    Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
    """
    try:
        result = div_1 / div_2
    except ZeroDivisionError:
        print("Деление на ноль.")
    else:
        return result


num_1 = float(input('Введите делимое: '))
num_2 = float(input('Введите делитель: '))
print('Результата деления: ', division(num_1, num_2))
