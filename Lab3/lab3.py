import copy
from abc import ABC, abstractmethod

# Абстрактний клас Prototype
class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass

# Клас кола
class Circle(Shape):
    def __init__(self, radius: float, color: str):
        super().__init__(color)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Коло: радіус = {self.radius}, колір = {self.color}")

# Клас прямокутника
class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str):
        super().__init__(color)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print(f"Прямокутник: ширина = {self.width}, висота = {self.height}, колір = {self.color}")

# Основна програма
def main():
    # Оригінальні об'єкти
    original_circle = Circle(5, "червоний")
    original_rectangle = Rectangle(3, 7, "синій")

    # Копії (прототипи)
    cloned_circle = original_circle.clone()
    cloned_rectangle = original_rectangle.clone()

    # Зміна кольору в копії
    cloned_circle.color = "зелений"
    cloned_rectangle.color = "жовтий"

    # Виведення
    print("Оригінали:")
    original_circle.display()
    original_rectangle.display()

    print("\nКопії:")
    cloned_circle.display()
    cloned_rectangle.display()

if __name__ == "__main__":
    main()
