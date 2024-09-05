# Stack

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The default stack interface
* Adjusting the stack data structure to support more complex operations
* Using the stack data structure in practice

## Overview

The coding exercises cover the following practical problems:
* Implementing the default stack interface
* Validating expressions in parentheses
* Adjusting a stack to support the `get_minimum` operation
* Reverse Polish notation (RPN) parsing

## Coding exercises

### Exercise 1: Implement the default stack interface

The following snippet contains the default interface for implementing the stack data structure. Of course, the interface can be expanded with additional methods if necessary.

```python
class Stack:
    """Default interface for Stack data structure."""

    def __init__(self):
        pass

    def empty(self) -> bool:
        """Returns True if the stack is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def size(self) -> int:
        """Returns the number of elements within the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def push(self, element: Any):
        """Adds a given element to the top of the stack.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def pop(self) -> Any:
        """Returns the top element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        pass

    def peak(self) -> Any:
        """Returns the top element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the stack is empty.
        """
        pass
```

Your task is to implement the provided default interface for the stack above.

<br/>

Please use the template `tasks/stack.py:Stack` for the implementation.

## Exercise 2: Check whether a given parentheses expression is valid

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


Your task is to implement the following function to solve the problem above:

```python
def is_valid_parentheses(expression: str) -> bool:
    """Returns True if a given string is valid parentheses expression.

    Args:
        expression: str, input string for validation.
    Returns:
        bool, whether a given string is valid parentheses expression.
    """
    pass
```

**Example 1:**

`s`='()'

Expected output: True.

**Example 2:**

`s`='()[]{}'

Expected output: True.

**Example 3:**

`s`='([})'

Expected output: False.

<br/>

Please use the template `tasks/parentheses.py:is_valid_parentheses` for the implementation.

## Exercise 3: A stack with the `get_minimum` operation

Your task is to extend the default interface for a stack data structure and add the `get_minimum` method:

```python
class StackWithMinimum(Stack):  # Here we inherit from the default interface, make sure it is implemented already.
    """Extended Stack class that supports `get_minimum` operation.

    Assume that elements in Stack are numerical (so that `get_minimum` operation is eligible).
    """

    def get_minimum(self) -> Optional[int]:
        """Returns the minimum element in the stack.

        NOTE: if the stack is empty - return None.
        NOTE: O(1) complexity is expected for this operation.
        """
        pass
```

**Example:**

```python
stack = StackWithMinimum()
stack.push(3)  # 3
stack.push(2)  # 3, 2
stack.push(4)  # 3, 2, 4

assert stack.get_minimum() == 2

stack.push(5)  # 3, 2, 4, 5
stack.push(1)  # 3, 2, 4, 5, 1

assert stack.get_minimum() == 1

stack.pop()  # 3, 2, 4, 5
stack.pop()  # 3, 2, 4

assert stack.get_minimum() == 2
```

<br/>

Please use the template `tasks/stack.py:StackWithMinimum` for the implementation.


## Exercise 4: RPN parsing

Your task is to evaluate the value of an arithmetic expression in [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. This means the expression will always evaluate to a result and there will never be any division by zero operation.

You are provided with the following template for the implementation:

```python
def evaluate_rpn_tokens(rpn_tokens: List[str]) -> int:
    """Returns the evaluation result of a given list of RPN tokens."""
    pass
```


**Example 1:**

`tokens` = ["3","2","+","10","*"]

Expected output: 50.

Explanation: `(3 + 2) * 10 = 50`

**Example 2:**

`tokens` = ["10", "4", "-", "2", "*", "5", "/"]

Expected output: 2.

Explanation: `((10 - 4) * 2) / 5 = 2`

<br/>

Please use the template `tasks/rpn.py:evaluate_rpn_tokens` for the implementation.
