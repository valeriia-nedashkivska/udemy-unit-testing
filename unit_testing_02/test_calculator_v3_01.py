import unittest
from unit_testing_02.calculator_v3 import Calculator

class TestsCalculatorBase(unittest.TestCase):
    def test_add_using_two_positive_numbers(self):
        calc = Calculator(10, 20)
        result = calc.calc_add()
        self.assertEqual(result, 30)

    def test_add_using_one_negative_numbers(self):
        calc = Calculator(10, -20)
        result = calc.calc_add()
        self.assertEqual(result, -10)