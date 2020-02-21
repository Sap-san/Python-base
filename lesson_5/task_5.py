"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран. """

with open('text_7.txt', 'w+') as f_txt:
    num = input('Введите число: ')
    while num:
        f_txt.write(num + ' ')
        num = input('Введите число (нажмите Enter без ввода числа для завершения): ')
    f_txt.seek(0)
    num_sum = sum(list(map(float, f_txt.readline().split())))
print(num_sum)
