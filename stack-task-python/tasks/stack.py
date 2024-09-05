"""Templates for programming assignments: stack API."""

from typing import Any, Optional


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


class StackWithMinimum(Stack):
    """Extended Stack class that supports `get_minimum` operation.

    Assume that elements in Stack are numerical (so that `get_minimum` operation is eligible).
    """

    def __init__(self):
        super().__init__()
        self._min_elements = []

    def push(self, element: Any):
        """Adds a given element to the top of the stack and updates the minimum stack."""
        super().push(element)
        if not self._min_elements or element <= self._min_elements[-1]:
            self._min_elements.append(element)

    def pop(self) -> Any:
        """Returns the top element, removes it, and updates the minimum stack."""
        if self.empty():
            raise ValueError("Stack is empty")
        element = super().pop()
        if element == self._min_elements[-1]:
            self._min_elements.pop()
        return element

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        if self.empty():
            return None
        return self._min_elements[-1]
