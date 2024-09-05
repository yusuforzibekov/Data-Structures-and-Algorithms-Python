import pytest

from tasks.binary_tree_node import TreeNode


@pytest.fixture
def sample_tree1() -> TreeNode:
    """First sample tree."""
    return TreeNode(
        107,
        TreeNode(109),
        TreeNode(110)
    )


@pytest.fixture
def sample_tree2() -> TreeNode:
    """Second sample tree."""
    return TreeNode(
        107,
        TreeNode(109, TreeNode(1234)),
        TreeNode(110)
    )


@pytest.fixture
def sample_tree3() -> TreeNode:
    """Third sample tree."""
    return TreeNode(
        110,
        TreeNode(
            108,
            TreeNode(
                106,
                TreeNode(105)
            ),
            TreeNode(109)
        ),
        TreeNode(111)
    )
