# Практика 16

#Создание базового класса "Фигура" и его наследование для создания классов
#"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
#такие как вычисление площади и периметра, а классы-наследники будут иметь
#специфичные методы и свойства.


import math

class Figure:
    def __init__(self, name="Фигура"):
        self.name = name

    def area(self):
        return 0

    def perimeter(self):
        return 0

class Square(Figure):
    def __init__(self, side):
        super().__init__("Квадрат")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def get_diagonal(self):
        return round(self.side * math.sqrt(2), 2)

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.width == self.height

class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def get_diameter(self):
        return self.radius * 2

sq = Square(5)
rect = Rectangle(4, 6)
circ = Circle(3)

figures_list = [sq, rect, circ]

for fig in figures_list:
    print(f"\nФигура: {fig.name}")
    print(f"Площадь: {fig.area()}")
    print(f"Периметр: {fig.perimeter()}")

    if isinstance(fig, Square):
        print(f"Диагональ: {fig.get_diagonal()}")
    elif isinstance(fig, Rectangle):
        print(f"Это квадрат?: {fig.is_square()}")
    elif isinstance(fig, Circle):
        print(f"Диаметр: {fig.get_diameter()}")
