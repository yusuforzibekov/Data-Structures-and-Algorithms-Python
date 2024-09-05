"""Templates for programming assignments: binary tree properties."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Checks whether a given binary tree is height-balanced.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        Boolean, whether a given binary tree is height-balanced.
    """
    def height_and_balance(node):
        if not node:
            return 0, True
        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)
        current_height = max(left_height, right_height) + 1
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return current_height, is_balanced
    
    _, balanced = height_and_balance(root)
    return balanced


def is_binary_search_tree(root: Optional[TreeNode]) -> bool:
    """Checks whether a given tree is a binary search tree.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        Boolean, whether a given tree is a binary search tree.
    """
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.value < high):
            return False
        return validate(node.left, low, node.value) and validate(node.right, node.value, high)
    
    return validate(root, float('-inf'), float('inf'))
