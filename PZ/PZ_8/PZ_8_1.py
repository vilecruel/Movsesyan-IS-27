#Практическая 8

#Отсортируйте словарь {'Physics':82, 'Math':65, 'history':75} по значению
#по возрастанию
dano = {'Physics': 82, 'Math': 65, 'history': 75}

otsortirovano = sorted(dano, key=dano.get)

otvet = {}
otvet[otsortirovano[0]] = dano[otsortirovano[0]]
otvet[otsortirovano[1]] = dano[otsortirovano[1]]
otvet[otsortirovano[2]] = dano[otsortirovano[2]]

print("Исходный словарь:", dano)
print("Отсортированный словарь:", otvet)