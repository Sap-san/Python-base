"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников."""

with open('text_3.txt') as f_txt:
    workers_info = f_txt.readlines()
    print(workers_info)

    f_txt.seek(0)
    income = workers = 0
    for line in f_txt:
        worker_info = line.split()
        income += float(worker_info[1])
        workers += 1
        if float(worker_info[1]) < 20000:
            print(worker_info[0])
print(f'Средняя величина дохода всех сотрудников: {round(income/workers, 2)}')