import pytest
from triangles import Triangle
from points import Point


def test_triangle_initialization():
    triangle = Triangle(0, 0, 1, 1, 2, 0)
    assert triangle.pt1 == Point(0, 0)
    assert triangle.pt2 == Point(1, 1)
    assert triangle.pt3 == Point(2, 0)


def test_triangle_from_points():
    points = [Point(0, 0), Point(3, 0), Point(0, 4)]
    triangle = Triangle.from_points(points)
    assert triangle.pt1 == points[0]
    assert triangle.pt2 == points[1]
    assert triangle.pt3 == points[2]


def test_invalid_points():
    with pytest.raises(ValueError):
        Triangle.from_points([Point(0, 0), Point(1, 1)])


def test_area_calculation():
    triangle = Triangle(0, 0, 3, 0, 0, 4)
    assert triangle.area() == 6.0

    degenerate = Triangle(0, 0, 1, 0, 2, 0)
    assert degenerate.area() == 0.0


def test_center_property():
    triangle = Triangle(0, 0, 6, 0, 0, 6)
    assert triangle.center == Point(2, 2)


def test_move_method():
    triangle = Triangle(1, 1, 4, 1, 1, 5)
    moved_triangle = triangle.move(2, 3)
    assert moved_triangle.pt1 == Point(3, 4)
    assert moved_triangle.pt2 == Point(6, 4)
    assert moved_triangle.pt3 == Point(3, 8)


def test_bounding_box():
    triangle = Triangle(-3, 5, 7, -1, 2, 4)
    assert triangle.top == -1
    assert triangle.bottom == 5
    assert triangle.left == -3
    assert triangle.right == 7
    assert triangle.width == 10
    assert triangle.height == 6
    assert triangle.topleft == Point(-3, -1)
    assert triangle.bottomleft == Point(-3, 5)
    assert triangle.topright == Point(7, -1)
    assert triangle.bottomright == Point(7, 5)


def test_equality():
    triangle1 = Triangle(0, 0, 1, 1, 2, 0)
    triangle2 = Triangle(1, 1, 2, 0, 0, 0)
    assert triangle1 == triangle2

    triangle3 = Triangle(0, 0, 2, 0, 3, 1)
    assert triangle1 != triangle3