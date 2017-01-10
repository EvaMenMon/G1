import unittest
import suma as suma
import multiplicacion as multiplicacion

class test(unittest.TestCase):
    def testSuma1(self):
        self.assertEqual(3, suma.suma(1,2))
    
    def testSuma2(self):
        self.assertEqual(8, suma.suma(4,4))
        
    def testSuma3(self):
        self.assertEqual(9, suma.suma(3,6))
    
    def testMultiplicacion1(self):
        self.assertEqual(1, multiplicacion.multiplicacion(1,1))
        
    def testMultiplicacion2(self):
        self.assertEqual(15, multiplicacion.multiplicacion(3,5))
        
    def testMultiplicacion3(self):
        self.assertEqual(8, multiplicacion.multiplicacion(2,4))
        
if __name__ == '__main__':
    unittest.main()