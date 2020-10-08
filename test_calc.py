import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_suma(self):
        result=calc.suma(20,2)
        self.assertEqual(result,22)

    def test_roznica(self):
        result = calc.roznica(20, 2)
        self.assertEqual(result, 108)

    def test_iloczyn(self):
        result=calc.iloczyn(20,2)
        self.assertEqual(result,400)

    def test_iloraz(self):
        result=calc.iloraz(20,2)
        self.assertEqual(result,10)