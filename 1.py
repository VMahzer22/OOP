from abc import ABC, abstractmethod 

class Animal(ABC):
    def __init__(self, name):
        self.name = name 

    @abstractmethod
    def speak(self): 
        pass

    def describe(self): 
        return f"This is {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  

    def speak(self):  
        return "Woof!"

    def get_breed(self):  
        return self.__breed

    def set_breed(self, new_breed):  
        self.__breed = new_breed

# Похідний клас Cat
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color  

    def speak(self):  
        return "Meow!"

    def get_color(self): 
        return self.__color

    def set_color(self, new_color): 
        self.__color = new_color

animals = [
    Dog("Buddy", "Beagle"),
    Cat("Whiskers", "Black")
]

for animal in animals:
    print(animal.describe())
    print(animal.speak())     
