#Создайте класс «Матрица», который имеет атрибуты количества
#строк и столбцов. Добавьте методы для сложения, вычитания и умножения матриц.


import random

class Matrix:
    def __init__(self, rows, cols, fill_random=True):
        self.rows = rows
        self.cols = cols
        if fill_random:
            self.data = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data]) + '\n'

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Ошибка: размеры матриц не совпадают для сложения!")

        result = Matrix(self.rows, self.cols, fill_random=False)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Ошибка: размеры матриц не совпадают для вычитания!")

        result = Matrix(self.rows, self.cols, fill_random=False)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Ошибка: количество столбцов первой матрицы должно быть равно строкам второй!")

        result = Matrix(self.rows, other.cols, fill_random=False)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


print("Создаем матрицу A (3x3):")
matrix_A = Matrix(3, 3)
print(matrix_A)

print("Создаем матрицу B (3x3):")
matrix_B = Matrix(3, 3)
print(matrix_B)

print("Результат сложения (A + B):")
matrix_sum = matrix_A + matrix_B
print(matrix_sum)

print("Результат вычитания (A - B):")
matrix_sub = matrix_A - matrix_B
print(matrix_sub)

print("Результат умножения (A * B):")
matrix_mul = matrix_A * matrix_B
print(matrix_mul)
