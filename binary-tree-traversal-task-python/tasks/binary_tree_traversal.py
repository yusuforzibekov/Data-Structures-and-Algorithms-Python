"""Templates for programming assignments: binary tree traversal methods."""

from typing import List, Optional
from collections import deque

from tasks.binary_tree_node import TreeNode


def get_inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Returns values of a given binary tree using inorder traversal.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        List with numbers that correspond to inorder nodes traversal.
    """
    if root is None:
        return []
    return (
        get_inorder_traversal(root.left)
        + [root.value]
        + get_inorder_traversal(root.right)
    )


def get_postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Returns values of a given binary tree using postorder traversal.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        List with numbers that correspond to postorder nodes traversal.
    """
    if root is None:
        return []
    return (
        get_postorder_traversal(root.left)
        + get_postorder_traversal(root.right)
        + [root.value]
    )


def get_preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Returns values of a given binary tree using preorder traversal.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        List with numbers that correspond to preorder nodes traversal.
    """
    if root is None:
        return []
    return (
        [root.value]
        + get_preorder_traversal(root.left)
        + get_preorder_traversal(root.right)
    )


def get_level_order_traversal(root: Optional[TreeNode]) -> List[int]:
    """Returns values of a given binary tree using level order traversal.

    Args:
        root: TreeNode, root node of a given tree.

    Returns:
        List with numbers that correspond to level order nodes traversal.
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
