# fichier test_multiplication.py
import unittest
from multiplication import multiply

class TestMultiplication(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(7, 7), 49)
    
    def test_multiply_invalid_input(self):
        with self.assertRaises(ValueError):
            multiply("a", 3)
        with self.assertRaises(ValueError):
            multiply(2, "b")
        with self.assertRaises(ValueError):
            multiply("x", "y")

if __name__ == "__main__":
    unittest.main()
