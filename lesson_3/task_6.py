def int_func(word):
    """
    Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
    но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
    """
    latin_dic = {'q': 'Q', 'w': 'W', 'e': 'E', 'r': 'R', 't': 'T', 'y': 'Y', 'u': 'U', 'i': 'I', 'o': 'O', 'p': 'P',
                 'a': 'A', 's': 'S', 'd': 'D', 'f': 'F', 'g': 'G', 'h': 'H', 'j': 'J', 'k': 'K', 'l': 'L', 'z': 'Z',
                 'x': 'X', 'c': 'C', 'v': 'V', 'b': 'B', 'n': 'N', 'm': 'M'}
    word_title = latin_dic[word[0]] + word[1:]
    return word_title


user_str = input('Введите строку из слов, разделенных пробелом: ')
title_str = list(map(int_func, user_str.split()))
print(' '.join(title_str))

# реализация без функции
print(user_str.title())
