import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):       #konstruktor
        self.x = x
        self.y = y

    def __str__(self):      # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):     # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):        # obsługa point1 == point2
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

     # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):       # v1 - v2
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def cross(self, other):     # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        if isinstance(other, Point):
            return self.x * other.y - self.y * other.x
        return NotImplemented

    def length(self):       # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):     # bazujemy na tuple, immutable points
        return hash((self.x, self.y))   