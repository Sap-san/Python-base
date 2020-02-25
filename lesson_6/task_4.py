"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Поехали!', end=' ')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        if direction == 'r':
            print('Поворачиваем направо.', end=' ')
        elif direction == 'l':
            print('Поворачиваем налево.', end=' ')

    def show_speed(self):
        print(f'Скорость = {self.speed}.', end=' ')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость = {self.speed}.', end=' ')
        if self.speed > 60:
            print('Скорость превышена!', end=' ')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость = {self.speed}.', end=' ')
        if self.speed > 40:
            print('Скорость превышена!', end=' ')


class PoliceCar(Car):
    is_police = True


tc = TownCar(77, 'синий', 'Лада')
sc = SportCar(255, 'красный', 'Феррари')
wc = WorkCar(55, 'коричневый', 'Камаз')
pc = PoliceCar(111, 'жёлтый', 'УАЗ')

print(f'{tc.name}, цвет - {tc.color}, скорость - {tc.speed}.')
print(f'{sc.name}, цвет - {sc.color}, скорость - {sc.speed}. Полиция - {sc.is_police}.')
print(f'{wc.name}, цвет - {wc.color}, скорость - {wc.speed}.')
print(f'{pc.name}, цвет - {pc.color}, скорость - {pc.speed}. Полиция - {pc.is_police}.')

tc.go()
tc.turn('l')
tc.show_speed()
tc.stop()

sc.go()
sc.turn('r')
sc.show_speed()
sc.stop()

wc.go()
wc.turn('l')
wc.show_speed()
wc.stop()

pc.go()
pc.turn('r')
pc.show_speed()
pc.stop()
