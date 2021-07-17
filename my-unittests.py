from calc import Calc
import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_suma(self):
        self.assertEqual(4, self.calc.sumar(2,2))
        self.assertEqual(13, self.calc.sumar(1,12))
        self.assertEqual(1100, self.calc.sumar(100,1000))
        self.assertEqual(0, self.calc.sumar(0,0))
        self.assertEqual("Invalid", self.calc.sumar(1,-1))


    def test_resta(self):
        self.assertEqual(0, self.calc.restar(2,2))
        self.assertEqual(11, self.calc.restar(12,1))
        self.assertEqual(900, self.calc.restar(1000,100))
        self.assertEqual(0, self.calc.restar(0,0))
        self.assertEqual("Invalid", self.calc.restar(1,-1))
        
    def test_multiplicar(self):
        self.assertEqual(4, self.calc.multiplicar(2,2))
        self.assertEqual(12, self.calc.multiplicar(1,12))
        self.assertEqual(100000, self.calc.multiplicar(100,1000))
        self.assertEqual(0, self.calc.multiplicar(0,0))
        self.assertEqual("Invalid", self.calc.multiplicar(1,-1))

if __name__ == '__main__':
    unittest.main()
     