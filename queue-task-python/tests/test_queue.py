"""Sample tests for 'tasks.queue' module."""
import pytest

from tasks.queue import Queue, QueueViaStacks
from tasks.stack import Stack


def test_queue_sample():
    """Sample tests for Queue class."""
    queue = Queue()

    with pytest.raises(ValueError):
        _ = queue.pop()

    assert queue.empty()

    for element in range(5):
        queue.push(element)

    assert queue.size() == 5

    for expected_element in range(5):
        element = queue.pop()
        assert expected_element == element

    # Pop when stack is empty.
    with pytest.raises(ValueError):
        _ = queue.peak()


def additional_tests_for_stack_sample():
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


def test_queue_via_stacks_sample():
    """Sample tests for QueueViaStacks class."""
    additional_tests_for_stack_sample()

    queue = QueueViaStacks()

    with pytest.raises(ValueError):
        _ = queue.pop()

    assert queue.empty()

    for element in range(5):
        queue.push(element)

    assert queue.first_stack.size() + queue.second_stack.size() == 5

    assert queue.size() == 5

    for expected_element in range(5):
        element = queue.pop()
        assert expected_element == element

    # Pop when stack is empty.
    with pytest.raises(ValueError):
        _ = queue.peak()

    assert queue.first_stack.empty()
    assert queue.second_stack.empty()
