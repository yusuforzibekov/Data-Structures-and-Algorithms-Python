"""Template for programming assignment: Lines"""
from tasks.point import Point


class Line:
    """
    Represents lines in a plane by their linear
    equations in the format: a * x + b * y + c = 0
    """
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def are_parallel(l1: 'Line', l2: 'Line') -> bool:
        """Checks that two lines are parallel"""
        # Lines are parallel if their slopes are equal
        # Slope is represented by the ratio of coefficients -a/b
        return l1.a * l2.b == l2.a * l1.b

    @classmethod
    def from_two_points(cls, p1: Point, p2: Point) -> 'Line':
        """Constructs a Line object based on two points
        through which the line should pass"""
        # Using point-slope form to general form conversion
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = p2.x * p1.y - p1.x * p2.y
        return cls(a, b, c)

    def __eq__(self, other: 'Line') -> bool:
        """Checks if two line are equal, i.e. their equations
        are equivalent"""
        return (
            (self.a * other.b == self.b * other.a) and
            (self.c * other.b == self.b * other.c) and
            (self.a * other.c == self.c * other.a)
        )

    def __repr__(self) -> str:
        return f'Line({self.a}, {self.b}, {self.c})'
