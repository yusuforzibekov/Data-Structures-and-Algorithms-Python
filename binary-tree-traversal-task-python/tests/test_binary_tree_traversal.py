"""Sample tests for 'tasks.binary_tree_traversal' module."""

from tasks.binary_tree_traversal import (get_inorder_traversal,
                                         get_level_order_traversal,
                                         get_postorder_traversal,
                                         get_preorder_traversal)


def test_get_inorder_traversal_sample(sample_tree1, sample_tree2):
    """Sample tests for get_inorder_traversal function."""
    assert not get_inorder_traversal(None)

    assert get_inorder_traversal(sample_tree1) == [109, 107, 110]

    assert get_inorder_traversal(sample_tree2) == [1234, 109, 107, 110]


def test_get_preorder_traversal_sample(sample_tree1, sample_tree2):
    """Sample tests for get_preorder_traversal function."""
    assert not get_preorder_traversal(None)

    assert get_preorder_traversal(sample_tree1) == [107, 109, 110]

    assert get_preorder_traversal(sample_tree2) == [107, 109, 1234, 110]


def test_get_postorder_traversal_sample(sample_tree1, sample_tree2):
    """Sample tests for get_postorder_traversal function."""
    assert not get_postorder_traversal(None)

    assert get_postorder_traversal(sample_tree1) == [109, 110, 107]

    assert get_postorder_traversal(sample_tree2) == [1234, 109, 110, 107]


def test_get_level_order_traversal_sample(sample_tree1, sample_tree2):
    """Sample tests for get_level_order_traversal function."""
    assert not get_level_order_traversal(None)

    assert get_level_order_traversal(sample_tree1) == [107, 109, 110]

    assert get_level_order_traversal(sample_tree2) == [107, 109, 110, 1234]
