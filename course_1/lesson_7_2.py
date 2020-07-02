# Урок 7. Задание 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def material(self):
        return f'Расход ткани на пальто составит: {round(self.v / 6.5 + 0.5, 3)}'

    def __str__(self):
        return f'Ваш размер: {self.v}'

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, size):
        if size < 44:
            self.__v = 44
        elif size > 62:
            self.__v = 62
        else:
            self.__v = size


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def material(self):
        return f'Расход ткани на костюм составит: {2 * self.h + 0.3}'

    def __str__(self):
        return f'Ваш рост: {self.h}'

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, height):
        if height < 170:
            self.__h = 170
        elif height > 188:
            self.__h = 188
        else:
            self.__h = height


my_coat = Coat(48)
print(my_coat)
print(my_coat.material())

my_suit = Suit(178)
print(my_suit)
print(my_suit.material())

big_coat = Coat(2020)
print(big_coat)
print(big_coat.material())

big_suit = Suit(2020)
print(big_suit)
print(big_suit.material())
