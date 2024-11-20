import unittest
from points import *

class TestPoint(unittest.TestCase):
    def test_str(self):
        p = Point(2, 2)
        self.assertEqual(str(p), "(2, 2)")

    def test_repr(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(1, 2)")

    def test_eq(self):
        p1 = Point(7, 5)
        p2 = Point(7, 5)
        p3 = Point(2, 3)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_ne(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertTrue(p1 != p2)

    def test_add(self):
        p1 = Point(1, 8)
        p2 = Point(2, 3)
        self.assertEqual(p1 + p2, Point(3, 11))

    def test_sub(self):
        p1 = Point(1, 4)
        p2 = Point(2, 3)
        self.assertEqual(p1 - p2, Point(-1, 1))

    def test_mul(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertEqual(p1 * p2, 1 * 2 + 2 * 3)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertEqual(p1.cross(p2), 1 * 3 - 2 * 2)

    def test_length(self):
        p = Point(3, 4)
        self.assertEqual(p.length(), 5)