import unittest
import code

class TestCode(unittest.TestCase):

    def test_gcd(self):

        result = code.gcd(0,0)
        self.assertEqual(result, None)

        result = code.gcd(17,32)
        self.assertEqual(result, 1)

#it's time for negative testing

        result = code.gcd(17,32)
        self.assertNotEqual(result, 6)
        
        self.assertFalse(code.gcd(4.5,8))
        self.assertFalse(code.gcd('one','five'))

    def test_fibonacci(self):

        result = code.fibonacci(0)
        self.assertEqual(result, 1)

        result = code.fibonacci(5)
        self.assertEqual(result, 8)

#it's time for negative testing

        result = code.fibonacci(5)
        self.assertNotEqual(result, 3)
        
        self.assertFalse(code.fibonacci('five'))  
        self.assertFalse(code.fibonacci(-5))

if __name__ == '__main__':
    unittest.main()