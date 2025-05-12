from abc import ABC, abstractmethod

# ======= Strategy =======

# Абстрактна стратегія форматування тексту
class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass

class UpperCaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.upper()

class LowerCaseFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.lower()

class CapitalizeFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.capitalize()

# ======= State =======

# Абстрактний стан редактора
class EditorState(ABC):
    @abstractmethod
    def handle(self, editor):
        pass

class EditingState(EditorState):
    def handle(self, editor):
        print("Редактор у режимі РЕДАГУВАННЯ.")
        print("Можна редагувати текст.")
        editor.state = SavedState()

class SavedState(EditorState):
    def handle(self, editor):
        print("Текст ЗБЕРЕЖЕНО.")
        print("Редагування заблоковане.")
        editor.state = ClosedState()

class ClosedState(EditorState):
    def handle(self, editor):
        print("Редактор ЗАКРИТО.")
        print("Не можна виконувати дії.")

# ======= Text Editor =======

class TextEditor:
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter
        self.state = EditingState()

    def set_formatter(self, formatter: TextFormatter):
        self.formatter = formatter

    def write_text(self, text: str):
        print("Відформатований текст:", self.formatter.format(text))

    def change_state(self):
        self.state.handle(self)

# ======= Основна програма =======

def main():
    editor = TextEditor(CapitalizeFormatter())

    editor.write_text("hello, world")
    editor.set_formatter(UpperCaseFormatter())
    editor.write_text("strategy pattern")
    editor.set_formatter(LowerCaseFormatter())
    editor.write_text("MIXED Case TeXT")

    print("\n=== Зміна станів редактора ===")
    editor.change_state()  # -> SavedState
    editor.change_state()  # -> ClosedState
    editor.change_state()  # -> Already Closed

if __name__ == "__main__":
    main()
