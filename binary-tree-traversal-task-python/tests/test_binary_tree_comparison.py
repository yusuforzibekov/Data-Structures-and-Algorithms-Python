"""Sample tests for 'tasks.binary_tree_comparison' module."""

from tasks.binary_tree_comparison import check_trees_equality
from tasks.binary_tree_node import TreeNode


def test_check_trees_equality_sample(sample_tree1, sample_tree2):
    """Sample tests for check_trees_equality function."""
    assert check_trees_equality(None, None)

    assert not check_trees_equality(TreeNode(107), None)

    assert check_trees_equality(TreeNode(107), TreeNode(107))

    assert check_trees_equality(sample_tree1, sample_tree1)

    assert not check_trees_equality(sample_tree1, sample_tree2)
