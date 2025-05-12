from abc import ABC, abstractmethod
import math

# Абстрактний клас для всіх фігур
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

# Клас кола
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

# Клас прямокутника
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

# Клас для виводу площі
class AreaPrinter:
    def print_area(self, shape: Shape):
        print(f"Площа фігури: {shape.area():.2f}")

# Основна програма
def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    printer = AreaPrinter()

    printer.print_area(circle)
    printer.print_area(rectangle)

if __name__ == "__main__":
    main()
