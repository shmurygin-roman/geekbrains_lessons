#  -------------------------------------------------------- 1 ----------------------------------------------------------


class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print(mtrx_1)
print('#' * 30)
print(mtrx_2)
print('#' * 30)
print(mtrx_1 + mtrx_2)
print('#' * 30)
print(new_m)
m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['9', '-54'], ['12', '3', '16']]
print('#' * 30)
mtrx_3 = Matrix(m_3)
mtrx_4 = Matrix(m_4)
print(mtrx_3 + mtrx_4)
print('#' * 30)
m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['12', '3', '16'], ['12', '3']]
print(mtrx_3 + mtrx_4)


#  ------------------------------------------- вариант решения ---------------------------------------------------------

    a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
    b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


    class Matrix:
        def __init__(self, lists):
            self.lists = lists

        def __str__(self):
            return '\n'.join(map(str, self.lists))

        def __add__(self, other):
            c = []
            for i in range(len(self.lists)):
                c.append([])
                for j in range(len(self.lists[0])):
                    c[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, c))


    matrix_1 = Matrix(a)
    matrix_2 = Matrix(b)
    print(f"Matrix 1\n{matrix_1}\n{'-'*20}")
    print(f"Matrix 2\n{matrix_2}\n{'-'*20}")
    print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
                      for j in range(len(self.matrix[0])))


stroki = int(input("Введите количество строк и столбцов матрицы: "))
stolbci = stroki

matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Summ of first and second matrix:\n', matrix1 + matrix2)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)

#  -------------------------------------------------------- 2 ----------------------------------------------------------


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a costume - {2 * self.param + 0.3}")
        return 2 * self.param + 0.3

coat = Coat(42)
costume = Costume(170)
print(coat + costume)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, param=100):
        self.param = param

    @property
    def consumption_Coat(self, param):
        pass

    @property
    def consumption_Costume(self, param):
        pass

    @property
    def consumption(self):
        return self.consumption_Coat + self.consumption_Costume


class Coat(Clothes):
    @property
    def consumption(self):
        result = round(self.param / 6.5 + 0.5, 2)
        Clothes.consumption_Coat = result
        return f'Расход ткани для пальто - {self.param} размера = {round(self.param / 6.5 + 0.5, 2)}'


class Costume(Clothes):
    @property
    def consumption(self):
        result = round(2 * self.param + 0.3, 2)
        Clothes.consumption_Costume = result
        return f'Расход ткани для костюм - на рост {self.param} = {round(2 * self.param + 0.3, 2)}'


my_1 = Clothes()
my_2 = Coat(35)
print(my_2.consumption)
my_3 = Costume(183)
print(my_3.consumption)
print(f'Общий расход ткани = {my_1.consumption}')

#  -------------------------------------------------------- 3 ----------------------------------------------------------


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Sum of cell is: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше равно второй, вычитание невозможно!"

    def __mul__(self, other):
        return f'Multiply of cells is: {self.nums * other.nums}'

    def __truediv__(self, other):
        return f'Truediv of cells is: {round(self.nums / other.nums)}'


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(7))

