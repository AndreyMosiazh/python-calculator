class Calculator:
    def add(self, x, y):
        """Додає два числа."""
        return x + y

    def subtract(self, x, y):
        """Віднімає одне число від іншого."""
        return x - y

    def multiply(self, x, y):
        """Множить два числа."""
        return x * y

    def divide(self, x, y):
        """Ділить одне число на інше."""
        if y == 0:
            raise ValueError("Ділення на нуль неможливе!")
        return x / y
