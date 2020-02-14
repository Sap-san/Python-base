income = float(input('Введите значение выручки фирмы: '))
expense = float(input('Введите значение издержек фирмы: '))
balance = income - expense
if balance > 0:
    print(f'Ваша фирма прибыльная!\nРентабельность: {balance/income}')
    staff = int(input('Сколько сотрудников в фирме? '))
    print(f'Прибыль на одного сотрудника: {round(balance/staff, 2)}')
elif balance < 0:
    print('Ваша фирма убыточная.')
else:
    print('Ваша фирма работает в 0.')
