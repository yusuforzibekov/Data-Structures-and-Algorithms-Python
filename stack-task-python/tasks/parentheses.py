"""Template for programming assignment: parentheses validation."""


def is_valid_parentheses(expression: str) -> bool:
    """Returns True if a given string is valid parentheses expression.

    Args:
        expression: str, input string for validation.
    Returns:
        bool, whether a given string is valid parentheses expression.
    """
    stack = []
    matching_parentheses = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses:
            if not stack or stack.pop() != matching_parentheses[char]:
                return False
        else:
            # Invalid character for the given problem.
            return False

    return not stack
