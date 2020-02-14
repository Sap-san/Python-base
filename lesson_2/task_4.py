user_str = input('Введите строку: ').split()
for num, word in enumerate(user_str):
    print(num, word[:10])
