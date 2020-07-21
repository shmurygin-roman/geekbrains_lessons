# Урок 6. Задание 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        follow = ('red', 'yellow', 'green', 'yellow')
        while True:
            for i in follow:
                if i == 'red':
                    print(f'\033[31m {i}')
                elif i == 'yellow':
                    print(f'\033[33m {i}')
                elif i == 'green':
                    print(f'\033[32m {i}')
                sleep(TrafficLight.__color.get(i))


light_1 = TrafficLight()
light_1.running()