"""Sample tests for 'tasks.reshape_matrix' module."""
from tasks.reshape_matrix import reshape_matrix


def test_reshape_matrix():
    """Sample tests for reshape_matrix function."""
    assert reshape_matrix([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert reshape_matrix([[1, 2], [3, 4], [5, 6]], 2, 3) == [[1, 2, 3], [4, 5, 6]]
    assert reshape_matrix([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
