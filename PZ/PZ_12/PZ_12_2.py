#Используем матрицу из предыдущей задачи
#Находим сумму первых двух строк в функциональном стиле через sum() и срез
#matrix[:2] берёт первую и вторую строки, а sum(row) складывает числа внутри
#них

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

current_value = random.randint(1, 10)
step = random.randint(1, 5)

matrix = []
for i in range(rows):
    row = [current_value + (i * cols + j) * step for j in range(cols)]
    matrix.append(row)

total_sum = sum(sum(row) for row in matrix[:2])

print(f"Сумма элементов первых двух строк: {total_sum}")