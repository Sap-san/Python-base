num = int(input('Введите число элементов в списке: '))

# поэлементный ввод
list_var = [input('Введите элемент списка: ') for i in range(num)]

# генерация списка для проверки
# list_var = [i for i in range(num)]

print('Начальный список:', list_var)
for i in range(0, len(list_var)-1, 2):
    list_var[i], list_var[i+1] = list_var[i+1], list_var[i]
print('Конечный список:', list_var)
