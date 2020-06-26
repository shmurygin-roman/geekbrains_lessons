# Урок 6. Задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {'wage': wage, 'bonus': bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = 'Тест'
    surname = 'Тестов'
    position = 'тестировщик'
    _income = {'wage': 5000, 'bonus': 2000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position()
worker_1.name = 'Иван'
worker_1.surname = 'Петров'
worker_1.position = 'Программист'
worker_1._income['wage'] = 20000
worker_1._income['bonus'] = 10000

print(worker_1.get_full_name())
print(worker_1.get_total_income())
