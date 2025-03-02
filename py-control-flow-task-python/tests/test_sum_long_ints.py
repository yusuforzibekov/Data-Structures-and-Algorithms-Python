"""Sample tests for 'tasks.sum_long_ints' module."""
from tasks.sum_long_ints import sum_long_integers


def test_sum_long_ints():
    """Sample tests for sum_long_integers function."""
    assert sum_long_integers([2, 1], [3, 6]) == [5, 7]
    assert sum_long_integers([1, 2], [9]) == [2, 1]
    assert sum_long_integers([3, 6], [1, 6, 3]) == [1, 9, 9]
