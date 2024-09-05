"""Sample tests for 'tasks.two_sum' module."""
from tasks.two_sum import find_target_sum


def test_find_target_sum_sample():
    """Sample tests for find_target_sum function."""
    assert find_target_sum([1, 2, 3, 4, 5], 4) == (0, 2)
    assert find_target_sum([1, 2, 3, 4, 5], 8) == (2, 4)