"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mas(self, thickness):
        sq_met_mas = 25               # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
        return self._length * self._width * sq_met_mas * thickness


rd = Road(20, 5000)
print(f'Масса асфальта: {round(rd.asphalt_mas(5) / 1000, 2)} тонн')
