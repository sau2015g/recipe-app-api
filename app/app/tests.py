"""
Sample tests

"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test calc module

    """

    def test_add_two_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_two_numbers(self):
        res = calc.subtract(5, 6)
        self.assertEqual(res, -1)





    
    