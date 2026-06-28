#Практическая 12

#Сгенерировать матрицу на произвольное количество элементов, в которой
#задаётся преобразование от предыдущего элемента к следующему на произвольное
#значение.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

current_value = random.randint(1, 10)
step = random.randint(1, 5)

print(f"Стартовое число: {current_value}, шаг изменения: {step}")

matrix = []
for i in range(rows):
    row = [current_value + (i * cols + j) * step for j in range(cols)]
    matrix.append(row)

print("Сгенерированная матрица:")
for row in matrix:
    print(row)