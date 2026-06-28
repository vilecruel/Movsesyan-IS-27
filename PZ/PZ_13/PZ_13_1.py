# Практическая 13

#Из исходного текстового файла (experience.txt) выбрать стаж работы.
#Посчитать количество полученных элементов.

import re

with open("experience.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

experience_list = []

for line in lines:
    match = re.search(r'\d+\s+(?:лет|года|год|месяцев|месяца|месяц).*', line)
    if match:
        experience_list.append(match.group())

count_elements = len(experience_list)

print("Найденный стаж работы:")
for item in experience_list:
    print("-", item)

print("\nКоличество полученных элементов:", count_elements)
