# от введения нечисловых значений не делал проверку
month = int(input('Введите номер месяца (от 1 до 12): '))
while not(1 <= month <= 12):
    month = int(input('Ошибочный ввод. Введите номер месяца (от 1 до 12): '))

# решение через словарь
month_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
              10: 'осень', 11: 'осень', 12: 'зима'}
print(f'Этот месяц относится к времени года - {month_dict[month]}.')

# решение через список
month_list = [(1, 2, 12), 'зима', (3, 4, 5), 'весна', (6, 7, 8), 'лето', (9, 10, 11), 'осень']
i = 0
while not(month in month_list[i]):
    i += 2
print(f'Этот месяц относится к времени года - {month_list[i + 1]}.')
