"""Sample tests for 'tasks.binary_tree' module."""

from tasks.binary_tree import is_balanced, is_binary_search_tree


def test_is_balanced_sample(sample_tree1, sample_tree2, sample_tree3):
    """Sample tests for is_balanced function."""
    assert is_balanced(None)

    assert is_balanced(sample_tree1)

    assert is_balanced(sample_tree2)

    assert not is_balanced(sample_tree3)


def test_is_binary_search_tree(sample_tree1, sample_tree2, sample_tree3):
    """Sample tests for is_binary_search_tree function."""
    assert is_binary_search_tree(None)

    assert not is_binary_search_tree(sample_tree1)

    assert not is_binary_search_tree(sample_tree2)

    assert is_binary_search_tree(sample_tree3)
