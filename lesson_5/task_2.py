"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('text_2.txt') as f_txt:
    words_in_line = [len(line.strip().split()) for line in f_txt]

print('Строк в файле:', len(words_in_line))
for line, words in enumerate(words_in_line, 1):
    print(f'Слов в строке {line}: {words}')
