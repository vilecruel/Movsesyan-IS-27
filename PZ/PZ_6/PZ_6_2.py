# Практическая работа 6
# Задание 2: Дан список размера N. Найти номера двух ближайших элементов
# (то есть элементов с наименьшим модулем разности) и вывести эти номера
# в порядке возрастания.

n = int(input("Введите размер списка N: "))
A = []
for i in range(n):
    x = int(input(f"A[{i+1}]: "))
    A.append(x)

min_raznost = abs(A[1] - A[0])
nomer1 = 0
nomer2 = 1

for i in range(n):
    for j in range(i + 1, n):
        raznost = abs(A[i] - A[j])
        if raznost < min_raznost:
            min_raznost = raznost
            nomer1 = i
            nomer2 = j

if nomer1 < nomer2:
    print(f"Номера ближайших элементов: {nomer1+1} {nomer2+1}")
else:
    print(f"Номера ближайших элементов: {nomer2+1} {nomer1+1}")
