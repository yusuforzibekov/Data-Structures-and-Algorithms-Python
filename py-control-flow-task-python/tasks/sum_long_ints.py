"""Template for programming assignment: sum two long numbers"""
from typing import List


def sum_long_integers(number_1: List[int], number_2: List[int]) -> List[int]:
    """Returns the sum of two long numbers represented as
    lists of their digits in the same form.

    Examples:
        [2, 1] + [3, 6] = [5, 7], since 21 + 36 = 57
        [1, 2] + [9] = [2, 1], since 12 + 9 = 21

    Args:
        number_1: List[int], the list of digits of the first term
        number_2: List[int], the list of digits of the second term
    Returns:
        List[int], the list of digits of the sum of input terms
    """
    num1 = number_1[::-1]  # Reverse lists
    num2 = number_2[::-1]
    result = []
    carry = 0
    i = 0
    
    # Process digits while there are digits or carry
    while i < max(len(num1), len(num2)) or carry:
        val1 = num1[i] if i < len(num1) else 0
        val2 = num2[i] if i < len(num2) else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        result.append(total % 10)
        i += 1
    
    return result[::-1]  # Reverse back before returning
