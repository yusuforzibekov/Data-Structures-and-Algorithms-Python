"""Templates for programming assignments: binary search tree operations."""

from typing import Optional

from tasks.binary_tree_node import TreeNode


def search_in_bst(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    """Returns a node within a given BST with a given value.

    Args:
        root: TreeNode, root node of a given binary search tree.
        value: Int, a given value of interest.

    Returns:
        TreeNode, a node with a given value, if exists.
    """
    current = root
    while current:
        if value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
        else:
            return current
    return None


def insert_in_bst(root: Optional[TreeNode], value: int) -> TreeNode:
    """Returns a new root after inserting a given value into a given binary search tree.

    If a given tree is empty, the result tree should contain only one node.

    Args:
        root: TreeNode, root node of a given binary search tree.
        value: Int, a given value to insert.

    Returns:
        TreeNode, a root of a new binary search tree after the insertion.
    """
    if not root:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_in_bst(root.left, value)
    else:
        root.right = insert_in_bst(root.right, value)
    
    return root
