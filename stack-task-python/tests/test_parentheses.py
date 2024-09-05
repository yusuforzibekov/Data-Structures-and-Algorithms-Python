"""Sample tests for 'tasks.parentheses' module."""
from tasks.parentheses import is_valid_parentheses


def test_is_valid_parentheses_sample():
    """Sample tests for is_valid_parentheses function."""
    assert is_valid_parentheses('()')
    assert is_valid_parentheses('()[]{}')
    assert not is_valid_parentheses('([})')
    assert not is_valid_parentheses('([)]')
