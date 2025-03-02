"""Sample tests for programming assignment: Segments"""
import pytest
from tasks.point import Point
from tasks.segment import Segment


def test_segment_length():
    # Sample tests
    assert Segment(Point(-1, 0), Point(1, 0)).length == pytest.approx(2)
    assert Segment(Point(0, 3), Point(4, 0)).length == pytest.approx(5)
