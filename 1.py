class BaseClass:
    def __init__(self):
        print("BaseClass initialized")

    def base_method(self):
        return "Method from BaseClass"


class DerivedClass1(BaseClass):
    def __init__(self):
        super().__init__()
        print("DerivedClass1 initialized")

    def method1(self):
        return "Method from DerivedClass1"


class DerivedClass2(BaseClass):
    def __init__(self):
        super().__init__()
        print("DerivedClass2 initialized")

    def method2(self):
        return "Method from DerivedClass2"


if __name__ == "__main__":
    obj1 = DerivedClass1()
    print(obj1.base_method())  # Виклик методу з BaseClass
    print(obj1.method1())  # Виклик методу з DerivedClass1
    
    obj2 = DerivedClass2()
    print(obj2.base_method())  # Виклик методу з BaseClass
    print(obj2.method2())  # Виклик методу з DerivedClass2
