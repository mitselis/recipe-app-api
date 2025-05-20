'''Sample tests'''
from django.test import SimpleTestCase

from app import calc

class CalcTEsts(SimpleTestCase):
    '''Test the calc module.'''

    def test_add_numbers(self):
        '''TEst adding numbers together.'''
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        '''TEst subtracting numbers together.'''
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)