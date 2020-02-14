num = input('Введите целое положительное число: ')
max_digit = int(num[0])
i = 1
while max_digit < 9 and i < len(num):
    digit = int(num[i])
    if digit > max_digit:
        max_digit = digit
    i += 1
print(f'Максимальная цифра в числе: {max_digit}')
