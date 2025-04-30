import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Налаштування для кожного тестового методу."""
        self.calculator = Calculator()

    def test_add(self):
        """Тестування методу додавання."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        """Тестування методу віднімання."""
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(1, -1), 2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        """Тестування методу множення."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        """Тестування методу ділення."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertEqual(self.calculator.divide(-4, 2), -2)

    def test_divide_by_zero(self):
        """Тестування випадку ділення на нуль."""
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
