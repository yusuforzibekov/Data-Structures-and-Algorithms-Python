"""Template for programming assignment: Reverse Polish notation."""

from typing import List


def evaluate_rpn_tokens(rpn_tokens: List[str]) -> int:
    """Returns the evaluation result of a given list of RPN tokens."""
    stack = []

    for token in rpn_tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))

    return stack[0]
