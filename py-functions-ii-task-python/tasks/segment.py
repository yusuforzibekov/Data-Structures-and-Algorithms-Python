"""Template for programming assignment: Segments"""
from tasks.point import Point


class Segment:
    """Represents segments in a plane by their two endpoints"""
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def length(self) -> float:
        """Calculates the length of the segment"""
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** 0.5
