#Практическая 11

#В последовательности на 
 целых чисел умножить все элементы на последний
# минимальный элемент.

n = int(input("Введите количество элементов n: "))

numbers = []
for i in range(n):
    numbers.append(int(input(f"Введите {i+1}-е число: ")))

min_val = min(numbers[::-1])

numbers = [x * min_val for x in numbers]

print("Готовый список:", numbers)