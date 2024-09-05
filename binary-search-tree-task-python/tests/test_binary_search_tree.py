"""Sample tests for 'tasks.binary_search_tree' module."""

from tasks.binary_search_tree import insert_in_bst, search_in_bst
from tasks.binary_tree_node import TreeNode


def test_insert_in_bst_sample():
    """Sample tests for insert_in_bst function."""
    # Case 1: empty tree
    result_tree_root = insert_in_bst(None, 5)
    assert result_tree_root.value == 5

    # Case 2: simple tree
    input_tree = TreeNode(3, TreeNode(2))
    result_tree_root = insert_in_bst(input_tree, 5)
    assert result_tree_root.left.value == 2
    assert result_tree_root.value == 3
    assert result_tree_root.right.value == 5


def test_search_in_bst_sample(sample_tree3):
    """Sample tests for search_in_bst function."""
    node = search_in_bst(sample_tree3, 106)
    assert node.value == 106
    assert node.left.value == 105
    assert node.right is None

    node = search_in_bst(sample_tree3, 111)
    assert node.value == 111
    assert node.left is None
    assert node.right is None

    assert search_in_bst(sample_tree3, 13341) is None
