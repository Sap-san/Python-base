"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список
сохранить в виде json-объекта в соответствующий файл. Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""

import json

with open('text_7.txt') as f_txt:
    firms_dict = {}
    res_profit = num_profit = 0
    for line in f_txt:
        firm = line.split()
        firm_profit = float(firm[2]) - float(firm[3])
        firms_dict[firm[0]] = firm_profit
        if firm_profit > 0:
            res_profit += firm_profit
            num_profit += 1
average_profit = {'average_profit': round(res_profit/num_profit, 2)}

with open('task_7.json', 'w') as write_f:
    json.dump([firms_dict, average_profit], write_f)