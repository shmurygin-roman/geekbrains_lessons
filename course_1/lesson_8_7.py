# Урок 8. Задание 7
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + other.a * self.b
        return Complex(a, b)

    def __str__(self):
        return f'({self.a}+{self.b}j)' if self.b > 0 else f'({self.a}-{abs(self.b)}j)'


x = Complex(-1, 2)
y = Complex(3, -1)
print(x)
print(y)
print(x + y)
print(x * y)
