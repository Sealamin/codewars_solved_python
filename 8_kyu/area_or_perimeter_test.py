import unittest
from area_or_perimeter import area_or_perimeter

class TestAreaOrPerimeter(unittest.TestCase):
    def test_same_dimensions(self):
        result = area_or_perimeter(5, 5)
        self.assertEqual(result, 25)

    def test_different_dimensions(self):
        result = area_or_perimeter(5, 10)
