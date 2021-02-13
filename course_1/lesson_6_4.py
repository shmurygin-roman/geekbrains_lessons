# Урок 6. Задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    name = 'Машина'
    color = 'Белый'
    speed = 90
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')


class TownCar(Car):
    def __init__(self):
        print('Это городская машина')

    def show_speed(self):
        speed = 60
        print(f'Текущая скорость = {self.speed}')
        if self.speed > speed:
            print(f'Внимание! Вы превышаете скорость на {self.speed - speed}')


class SportCar(Car):
    def __init__(self):
        print('Это спортивная машина')


class WorkCar(Car):
    def __init__(self):
        print('Это грузовая машина')

    def show_speed(self):
        speed = 40
        print(f'Текущая скорость = {self.speed}')
        if self.speed > speed:
            print(f'Внимание! Вы превышаете скорость на {self.speed - speed}')


class PoliceCar(Car):
    is_police = True

    def __init__(self):
        print('Это полицейская машина')


town_car_1 = TownCar()
print(town_car_1.name)
print(town_car_1.color)
town_car_1.show_speed()
town_car_1.speed = 60
town_car_1.show_speed()

print('')

sport_car_1 = SportCar()
sport_car_1.name = 'Ferrari'
sport_car_1.color = 'Красный'
sport_car_1.speed = 180
print(sport_car_1.name)
print(sport_car_1.color)
print(sport_car_1.speed)
sport_car_1.go()
sport_car_1.turn('налево')
sport_car_1.stop()

print('')

work_car_1 = WorkCar()
work_car_1.name = 'Газель'
work_car_1.color = 'Серый'
print(work_car_1.name)
print(work_car_1.color)
work_car_1.show_speed()
work_car_1.speed = 30
work_car_1.show_speed()

print('')

police_car_1 = PoliceCar()
print(police_car_1.is_police)
police_car_1.go()
police_car_1.turn('налево')
police_car_1.turn('направо')
police_car_1.stop()