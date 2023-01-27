from solutions import Geometry_Area, Rectangle, Triangle, Square
import pytest


def test_rectangle():
    assert issubclass(Rectangle, Geometry_Area)
    assert Rectangle.valid_area is Geometry_Area.valid_area

    rectangle = Rectangle(1, 9)
    assert rectangle.area == 9


def test_square():
    assert issubclass(Square, Geometry_Area)
    assert Square.valid_area is Geometry_Area.valid_area

    square = Square(2)
    assert square.area == 4


def test_triangle():
    assert issubclass(Triangle, Geometry_Area)
    assert Triangle.valid_area is Geometry_Area.valid_area

    triangle = Triangle(4, 10)
    assert triangle.area == 20


def test_not_valid_area():
    triangle = Triangle(-2, 5)

    assert triangle.area == -5
    with pytest.raises(ValueError):
        triangle.valid_area()
