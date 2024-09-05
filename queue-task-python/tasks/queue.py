from typing import Any, Optional
from tasks.stack import Stack


class Queue:
    """Default interface for Queue data structure."""

    def __init__(self):
        self._elements = []

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._elements) == 0

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self._elements)

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        self._elements.append(element)

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        return self._elements.pop(0)

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        return self._elements[0]


class QueueViaStacks:
    """Default Queue interface implemented with two stacks only.

    NOTE: Stack interface is defined within `tasks/stack.py:Stack`, you may re-use
    the existing implementation (you should have created it at this point).

    NOTE: all methods of Queue interface should be implemented.
    """

    def __init__(self):
        # NOTE: __init__ shouldn't be changed.
        self.first_stack = Stack()
        self.second_stack = Stack()

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self.first_stack.empty() and self.second_stack.empty()

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self.first_stack.size() + self.second_stack.size()

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        self.first_stack.push(element)

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        if self.second_stack.empty():
            while not self.first_stack.empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        if self.second_stack.empty():
            while not self.first_stack.empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.peak()
