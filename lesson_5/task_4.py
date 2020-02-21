"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4.txt') as f_txt:
    for line in f_txt:
        string = line.split()
        string[0] = dict_num[string[0]]
        with open('text_4_rus.txt', 'a') as f_rus_txt:
            f_rus_txt.write(' '.join(string) + '\n')
