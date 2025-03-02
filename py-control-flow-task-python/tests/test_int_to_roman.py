"""Sample tests for 'tasks.int_to_roman' module."""
from tasks.int_to_roman import integer_to_roman


def test_int_to_roman():
    """Sample tests for integer_to_roman function."""
    assert integer_to_roman(3) == 'III'
    assert integer_to_roman(58) == 'LVIII'
    assert integer_to_roman(1994) == 'MCMXCIV'
