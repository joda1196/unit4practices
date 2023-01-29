class Geometry_Area:
    def __init__(self):
        self.area = 0

    def valid_area(self):
        if self.area < 0:
            raise ValueError


class Rectangle(Geometry_Area):
    def __init__(self, l, w):
        self.area = l * w


class Triangle(Geometry_Area):
    def __init__(self, h, b):
        self.area = 0.5 * h * b


class Square(Geometry_Area):
    def __init__(self, s):
        self.area = s**2
