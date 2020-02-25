"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров). """


class Worker:
    name = 'Иван'
    surname = 'Иванов'
    position = 'Разработчик Python'
    _income = {'wage': 44000, 'bonus': 5500}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


pos = Position()
total_income = pos._income['wage'] + pos._income['bonus']
print(f'{pos.name} {pos.surname}: {pos.position}, доход: {total_income}')
print('Использование методов класса:')
print(f'{pos.get_full_name()}: {pos.position}, доход: {pos.get_total_income()}')
