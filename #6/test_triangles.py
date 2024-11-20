import unittest
from triangles import *

class TestTriangle(unittest.TestCase):
    def test_str(self):
        tr = Triangle(5, 5, 3, 8, 7, 1)
        self.assertEqual(str(tr), "[(5, 5), (3, 8), (7, 1)]")

    def test_repr(self):
        tr = Triangle(9, 8, 7, 6, 5, 4)
        self.assertEqual(repr(tr), "Triangle(9, 8, 7, 6, 5, 4)")

    def test_eq(self):
        tr1 = Triangle(0, 0, 3, 0, 0, 4)
        tr2 = Triangle(0, 0, 0, 4, 3, 0)
        tr3 = Triangle(6, 5, 4, 2, 1, 5)
        self.assertTrue(tr1 == tr2)
        self.assertFalse(tr1 == tr3)

    def test_ne(self):
        tr1 = Triangle(0, 0, 3, 0, 0, 4)
        tr2 = Triangle(1, 1, 4, 1, 1, 5)
        self.assertTrue(tr1 != tr2)

    def test_center(self):
        tr = Triangle(0, 0, 3, 0, 0, 3)
        center = tr.center()
        self.assertEqual((center.x, center.y), (1, 1))

    def test_area(self):
        tr = Triangle(0, 0, 3, 0, 0, 4)
        self.assertEqual(tr.area(), 6)

    def test_move(self):
        tr = Triangle(0, 0, 6, 0, 0, 2)
        tr_moved = tr.move(1, 1)
        self.assertEqual(str(tr_moved), "[(1, 1), (7, 1), (1, 3)]")