"""Sample tests for 'tasks.tree_validity' module."""

from tasks.tree_validity import is_valid_tree


def test_is_valid_tree_sample():
    """Sample tests for is_valid_tree function."""
    # Example 1
    assert is_valid_tree(n=5, edges=[(0, 1), (0, 2), (0, 3), (3, 4)])
    # Example 2
    assert not is_valid_tree(n=5, edges=[(0, 1), (0, 2), (0, 3), (2, 3)])
    # Example 3
    assert not is_valid_tree(n=6, edges=[(0, 1), (0, 2), (0, 3), (2, 3), (0, 3)])