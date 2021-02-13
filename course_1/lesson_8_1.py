# Урок 8. Задание 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date
        self.dd, self.mm, self.yy = Date.get_date(self.date)
        Date.valid_date(self)

    @classmethod
    def get_date(cls, param):
        dd, mm, yy = map(int, param.split('-'))
        return dd, mm, yy

    @staticmethod
    def valid_date(self):
        dd_mm = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if self.mm < 1:
            self.mm = 1
        elif self.mm > 12:
            self.mm = 12

        if self.dd < 1:
            self.dd = 1
        elif self.dd > dd_mm.get(self.mm):
            self.dd = dd_mm.get(self.mm)

        if self.yy < 2010:
            self.yy = 2010
        elif self.yy > 2030:
            self.yy = 2030

    def __str__(self):
        return f'{self.dd} {self.mm} {self.yy}'


date_1 = Date('32-05-2222')
print(date_1)
