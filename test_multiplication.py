# fichier test_rectangle.py
import unittest
from rectangle import area_rectangle

class TestRectangleArea(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area_rectangle(2, 3), 6)
        self.assertEqual(area_rectangle(5, 5), 25)
        self.assertEqual(area_rectangle(10, 2), 20)
    
    def test_area_rectangle_invalid_input(self):
        with self.assertRaises(ValueError):
            area_rectangle("a", 3)
        with self.assertRaises(ValueError):
            area_rectangle(2, "b")
        with self.assertRaises(ValueError):
            area_rectangle("x", "y")
        with self.assertRaises(ValueError):
            area_rectangle(-2, 3)
        with self.assertRaises(ValueError):
            area_rectangle(2, -3)
        with self.assertRaises(ValueError):
            area_rectangle(0, 3)

if __name__ == "__main__":
    unittest.main()
