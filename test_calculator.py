import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(853, 999), 1852)
        self.assertEqual(self.calc.add(57, 112), 169)

        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(8, 3), 5)

        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(8, 5), 40)

        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 10), 2)

        self.assertEqual(self.calc.modulo(22, 7), 1)
        self.assertEqual(self.calc.modulo(12, 6), 0)

if __name__ == '__main__':
    unittest.main()