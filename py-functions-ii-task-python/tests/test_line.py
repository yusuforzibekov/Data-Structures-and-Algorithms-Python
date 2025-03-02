"""Sample tests for programming assignment: Lines"""
from tasks.line import Line
from tasks.point import Point


def test_line_are_parallel():
    # Sample tests
    assert Line.are_parallel(Line(1, 0, 1), Line(1, 0, 2))
    assert not Line.are_parallel(Line(1, -1, 0), Line(1, 0, 1))
    assert Line.are_parallel(Line(1, -1, 0), Line(2, -2, 2))


def test_line_from_two_points():
    # Sample tests
    assert Line.from_two_points(Point(-1, 0), Point(-1, 1)) == Line(1, 0, 1)
    assert Line.from_two_points(Point(-1, 0), Point(0, 1)) == Line(1, -1, 1)
