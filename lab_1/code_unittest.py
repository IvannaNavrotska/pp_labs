import unittest
import code

class TestCode(unittest.TestCase):

    def test_gcd(self):

        result = code.gcd(0,0)
        self.assertEqual(result, None)

        result = code.gcd(-15,0)
        self.assertEqual(result, -15)

        result = code.gcd(12,6)
        self.assertEqual(result, 6)

        result = code.gcd(17,32)
        self.assertEqual(result, 1)

    def test_fibonacci(self):

        result = code.fibonacci(0)
        self.assertEqual(result, 1)

        result = code.fibonacci(5)
        self.assertEqual(result, 8)

        result = code.fibonacci(13)
        self.assertEqual(result, 377)

if __name__ == '__main__':
    unittest.main()
