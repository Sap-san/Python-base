add_prod = input('Добавить товар? (y/n) ')  # чтобы не удлинять код не стал проверять корректность ввода
prod_list = []
while add_prod == 'y':
    prod = {'название': None, 'цена': None, 'количество': None, 'eд': None}
    for k in prod.keys():
        text = f'{k.title()}: ' if k != 'eд' else 'Единицы измерения: '
        prod[k] = input(text) if (k == 'название' or k == 'eд') else int(input(text))
    prod_list.append(tuple([len(prod_list) + 1, prod]))
    add_prod = input('Добавить  следующий товар? (y/n) ')
print('Структура:', prod_list)

prod_analytics = {key: [] for key in prod.keys()}
for key in prod_analytics.keys():
    for row in prod_list:
        prod_analytics[key].append(row[1][key])
print('Аналитика:', prod_analytics)
