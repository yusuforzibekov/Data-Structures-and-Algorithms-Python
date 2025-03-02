"""Template for programming assignment:
Convert roman number to integer number"""


def roman_to_integer(roman: str) -> int:
    """Converts a Roman numeral to an integer.

    Examples:
        "III" -> 3
        "LVIII" -> 58
        "MCMXCIV" -> 1994

    Args:
        roman: str, Roman numeral
    Returns:
        int, integer representation of a Roman numeral
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0

    for char in reversed(roman):
        curr_value = values[char]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value

    return result
