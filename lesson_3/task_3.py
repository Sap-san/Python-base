def my_func(arg_1, arg_2, arg_3):
    """
    Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
    возвращает сумму наибольших двух аргументов.
    """
    args_list = (arg_1, arg_2, arg_3)
    return sum(args_list) - min(args_list)


numbers = []
for i in range(3):
    numbers.append(float(input('Введите число: ')))
print('Сумма наибольших двух аргументов: ', my_func(*numbers))
