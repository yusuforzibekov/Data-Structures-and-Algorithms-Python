"""Sample tests for 'tasks.stack' module."""
import pytest

from tasks.stack import Stack, StackWithMinimum


def test_stack_sample():
    """Sample tests for Stack class."""
    stack = Stack()

    with pytest.raises(ValueError):
        _ = stack.pop()

    assert stack.empty()

    for element in range(5):
        stack.push(element)

    assert stack.size() == 5

    for expected_element in range(4, -1, -1):
        element = stack.pop()
        assert expected_element == element

    # Pop when stack is empty.
    with pytest.raises(ValueError):
        _ = stack.peak()


def test_stack_with_minimum_sample():
    """Sample tests for StackWithMinimum class."""
    stack = StackWithMinimum()
    stack.push(3)
    stack.push(2)
    stack.push(4)

    assert stack.get_minimum() == 2

    stack.push(5)
    stack.push(1)

    assert stack.get_minimum() == 1

    stack.pop()
    stack.pop()

    assert stack.get_minimum() == 2
    assert stack.size() == 3
