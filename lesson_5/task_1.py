"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка."""

with open("text_1.txt", 'w') as f_txt:
    user_str = input()
    while user_str:
        f_txt.write(user_str + '\n')
        user_str = input()
