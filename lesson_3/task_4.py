def my_func(x, y):
    """
    Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
    возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
    необходимо обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
    """
    # первый способ
    result_1 = x ** y

    # второй способ
    result_2 = x
    for p in range(1, -y):
        result_2 *= x
    result_2 = 1 / result_2

    return result_1, result_2


num_1 = float(input('Введите действительное положительное число: '))
num_2 = int(input('Введите целое отрицательное число: '))
my_func_res = my_func(num_1, num_2)
print('Результат первого способа: ', my_func_res[0])
print('Результат второго способа: ', my_func_res[1])
