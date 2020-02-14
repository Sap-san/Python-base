my_list = [7, 5, 3, 3, 2]
enter = 'y'
while enter.lower() == 'y':
    new_num = int(input('Введите число: '))
    for i in range(len(my_list)):
        if new_num > my_list[i]:
            my_list.insert(i, new_num)
            break
        elif i == len(my_list) - 1:
            my_list.append(new_num)
    print(my_list)
    enter = input('Хотите ввести следующее число (y/n)? ')
    while enter.lower() != 'y' and enter.lower() != 'n':
        enter = input('Хотите ввести следующее число (y/n)? ')
