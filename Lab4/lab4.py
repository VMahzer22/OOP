from abc import ABC, abstractmethod

# ----- Composite -----

# Абстрактний компонент меню
class MenuComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Лист – окремий пункт меню
class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f"- {self.name}")

# Контейнер – підменю, яке містить інші компоненти
class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: MenuComponent):
        self.items.append(component)

    def display(self, indent=0):
        print('  ' * indent + f"[{self.name}]")
        for item in self.items:
            item.display(indent + 1)

# ----- Facade -----

class MenuFacade:
    def __init__(self):
        self.root_menu = self._create_full_menu()

    def _create_full_menu(self):
        # Створення головного меню
        main_menu = Menu("Головне меню")

        file_menu = Menu("Файл")
        file_menu.add(MenuItem("Новий"))
        file_menu.add(MenuItem("Відкрити"))
        file_menu.add(MenuItem("Зберегти"))

        edit_menu = Menu("Редагування")
        edit_menu.add(MenuItem("Вирізати"))
        edit_menu.add(MenuItem("Копіювати"))
        edit_menu.add(MenuItem("Вставити"))

        help_menu = Menu("Допомога")
        help_menu.add(MenuItem("Про програму"))

        main_menu.add(file_menu)
        main_menu.add(edit_menu)
        main_menu.add(help_menu)

        return main_menu

    def show_menu(self):
        print("=== МЕНЮ ПРОГРАМИ ===")
        self.root_menu.display()

# ----- Основна програма -----

def main():
    facade = MenuFacade()
    facade.show_menu()

if __name__ == "__main__":
    main()
