from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other):  # obsługa tr1 == tr2
        if not isinstance(other, Triangle):
            return NotImplemented
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        vertices_self = {self.pt1, self.pt2, self.pt3}
        vertices_other = {other.pt1, other.pt2, other.pt3}
        return vertices_self == vertices_other

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    @property       #zamiana metody na atrybut wirtualny
    def center(self):  # zwraca środek (masy) trójkąta
        x_center = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y_center = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x_center, y_center)

    def area(self):  # pole powierzchni
        x1, y1 = self.pt1.x, self.pt1.y
        x2, y2 = self.pt2.x, self.pt2.y
        x3, y3 = self.pt3.x, self.pt3.y
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def move(self, x, y):  # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y,
                        self.pt2.x + x, self.pt2.y + y,
                        self.pt3.x + x, self.pt3.y + y)


#metoda klasy
    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("ERROR! Trzy punkty są wymagane do stworzenia trójkąta!!!")
        return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)


#dekoratory
    @property
    def top(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)
    
    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)