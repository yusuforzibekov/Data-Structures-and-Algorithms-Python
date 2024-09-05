from typing import Any


class Stack:
    """Default interface for Stack data structure."""

    def __init__(self):
        self._elements = []

    def empty(self) -> bool:
        """Returns True if the stack is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._elements) == 0

    def size(self) -> int:
        """Returns the number of elements within the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._elements)

    def push(self, element: Any):
        """Adds a given element to the top of the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        self._elements.append(element)

    def pop(self) -> Any:
        """Returns the top element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.empty():
            raise ValueError("Stack is empty")
        return self._elements.pop()

    def peak(self) -> Any:
        """Returns the top element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.empty():
            raise ValueError("Stack is empty")
        return self._elements[-1]
