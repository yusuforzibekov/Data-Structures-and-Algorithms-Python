"""Templates for programming assignments: binary trees comparison."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def check_trees_equality(p_tree: Optional[TreeNode], q_tree: Optional[TreeNode]) -> bool:
    """Checks whether two given binary trees are the same.

    Trees equality is defined by both structural equality and by equality of values
    between corresponding tree nodes.

    Args:
        p_tree: TreeNode, root node of the first tree.
        q_tree: TreeNode, root node of the second tree.

    Returns:
        Boolean, whether given trees are equal.
    """
    if p_tree is None and q_tree is None:
        return True
    if p_tree is None or q_tree is None:
        return False
    return (p_tree.value == q_tree.value and
            check_trees_equality(p_tree.left, q_tree.left) and
            check_trees_equality(p_tree.right, q_tree.right))
