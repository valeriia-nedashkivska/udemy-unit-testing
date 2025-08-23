import unittest
import calcucator


class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calcucator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_number(self):
        result = calcucator.calc_add(-10, -20)
        self.assertEqual(result, -30)
