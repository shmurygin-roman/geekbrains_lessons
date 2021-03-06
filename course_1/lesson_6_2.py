# Урок 6. Задание 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    _length = 1
    _width = 1

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        result = round((self._length * self._width * 25 * 5) / 1000)
        return result


road_1 = Road(5000, 20)
road_2 = Road(100000, 20)
print(road_1.mass_calc())
print(road_2.mass_calc())
