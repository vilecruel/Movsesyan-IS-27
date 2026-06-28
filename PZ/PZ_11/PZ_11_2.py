#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.

def to_lower_generator(string):
    for char in string:
        yield char.lower()

user_str = input("Введите строку: ")

result_str = "".join(to_lower_generator(user_str))

print("Результат работы:", result_str)