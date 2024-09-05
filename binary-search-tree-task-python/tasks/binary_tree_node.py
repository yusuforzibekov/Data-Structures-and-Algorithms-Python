from typing import Optional


class TreeNode:
    """Dataclass that represents binary tree nodes."""

    def __init__(
        self,
        value: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.value = value
        self.left = left
        self.right = right
