import unittest
from enum import Enum
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    class Operation(Enum):
        Add = 1
        Subtract = 2
        Multiply = 3
        Divide = 4
        Sqrt = 5
        Log = 6
        Sin = 7
        Cos = 8

    def test_add(self):
        result = Calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = Calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = Calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = Calculator.divide(6, 2)
        self.assertEqual(result, 3)
    def test_sqrt(self):
        result = Calculator.sqrt(16)
        self.assertEqual(result, 4)
    
     def test_log(self):
        result = Calculator.log(1000000)
        self.assertEqual(result, 6)
        
    def test_invalid_operation(self):
        with self.assertRaises(AttributeError):
            Calculator.calculate(2, "InvalidOperation", 3)

if __name__ == '__main__':
    unittest.main()
