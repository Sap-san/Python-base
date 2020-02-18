"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

res_list = [i for i in range(100, 1001) if i % 2 == 0]
print(res_list)
multiplication = reduce(lambda a, b: a * b, res_list)
print(multiplication)
