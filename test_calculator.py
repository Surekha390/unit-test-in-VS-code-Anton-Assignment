import unittest
import calculator 
# Define a class that inherits from unittest.TestCase
class TestCalculatorFunctions(unittest.TestCase):

    # Define a test method
    def test_add_numbers(self):
        self.assertEqual(calculator.add_numbers(2, 3), 5)

    def test_mul_numbers(self):
        self.assertEqual(calculator.mul_numbers(5, 3), 15)

    def test_div_numbers(self):
        self.assertEqual(calculator.div_numbers(10, 5), 2)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(8, 2), 6)

if __name__ == "__main__":
    unittest.main() 