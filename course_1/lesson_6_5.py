# Урок 6. Задание 5
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}!')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}!!!')


pen = Pen()
pen.title = 'Ручка'
pen.draw()

pensil = Pencil()
pensil.title = 'Карандаш'
pensil.draw()

handle = Handle()
handle.title = 'Маркер'
handle.draw()
