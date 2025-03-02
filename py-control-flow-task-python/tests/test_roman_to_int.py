"""Sample tests for 'tasks.roman_to_int' module."""
from tasks.roman_to_int import roman_to_integer


def test_roman_to_int():
    """Sample tests for roman_to_integer function."""
    assert roman_to_integer('III') == 3
    assert roman_to_integer('LVIII') == 58
    assert roman_to_integer('MCMXCIV') == 1994
