# [Python] Classes and Object-Oriented Programming (OOP)

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

- The principles of OOP
- Classes and their syntax
- Operator overloading for classes

## Overview

The coding exercises cover the following practical problems:

- Functions and derivatives
- Polynomials

## Coding exercises

### Exercise 1: Functions and derivatives

In this task you will implement a mini-framework that covers a wide
class of mathematical functions and allows you to calculate their
derivatives. If you need to refresh your memory, please review the
differentiation rules in calculus
[here](https://www.mathsisfun.com/calculus/derivatives-rules.html).

Your task is to implement classes for elementary mathematical functions
and base operators that combine elementary functions to form more complex ones.
All classes for elementary mathematical functions should implement the
abstract interface `Function`, and all classes for operators should implement
the abstract interface `BinaryOperator`, which is derived from the `Function` class.

The following classes should be implemented:
- Elementary functions:
  - `Constant` – the constant function
  - `Power` – the power of x
  - `Sin` – the sine function
  - `Cos` – the cosine function
  - `Exp` – exponent functions with a fixed base
  - `Log` – logarithm functions with a fixed base
- Operators:
  - `Sum` – the sum of two functions
  - `Sub` – the difference between two functions
  - `Mul` – the product of two functions
  - `Div` – the quotient of two functions
  - `Comp` – the composition of two functions

Your goal is to implement two methods in every class:
- `__call__` – calculates the value of a mathematical function at a certain point.
- `derivative` – calculates the derivative of a mathematical function and returns
it as an instance of a class implementing the `Function` interface.

The example below shows a code template for a class that correspond to an elementary function.
```python
from abc import ABC

class Function(ABC):
    """Base abstract class for functions"""
    def derivative(self) -> 'Function':
        pass

    def __call__(self, x: float) -> float:
        pass

# Implement the following class
class Power(Function):
    """
    Class for power function: P(x) = x^n.
    Defaults to the identity function.
    """
    def __init__(self, n: float = 1):
        self.n = n

    def __call__(self, x: float) -> float:
        pass

    def derivative(self) -> Function:
        pass
```
The example below shows a code template for a class that correspond to an operator.
```python
from abc import ABC

class Function(ABC):
    """Base abstract class for functions"""
    def derivative(self) -> 'Function':
        pass

    def __call__(self, x: float) -> float:
        pass

class BinaryOperator(Function):
    """Base abstract class for binary operators"""
    def __init__(self, left: Function, right: Function):
        self.left = left
        self.right = right

# Implement the following class
class Sum(BinaryOperator):
    """Class for the sum of two arguments: f(x) + g(x)"""
    def __call__(self, x: float) -> float:
        pass

    def derivative(self) -> Function:
        pass
```

Please use the template `tasks/derivatives.py` for the implementation
and refer to the sample tests `tests/test_derivatives.py` to see some examples.

### Exercise 2: Polynomials

Your task is to implement that `Polynomial` class, which overloads built-in
operators and behaves like a mathematical polynomial function. In this
class, a mathematical polynomial is described by the list of its
coefficients in the order of decreasing degrees of x. If you feel
you need to review polynomials, please look at the resources
[The general form of polynomials](https://www.mathsisfun.com/algebra/polynomials.html),
[Addition, subtraction](https://www.mathsisfun.com/algebra/polynomials-adding-subtracting.html),
[Multiplication](https://www.mathsisfun.com/algebra/polynomials-multiplication-long.html), and
[Division](https://www.mathsisfun.com/algebra/polynomials-division-long.html)
to refresh your memory.

More precisely, in this task, you will implement the following methods:
- `Polynomial.trim` – removes the leading zeros from a list of coefficients
- `Polynomial.degree` – returns the degree of a polynomial
- `Polynomial.__call__` – calculates the value of a polynomial at a certain point (overloads the parenthesis operator)
- `Polynomial.__neg__` – negates a polynomial (overloads the unary `-` operator)
- `Polynomial.__add__` – adds two polynomials (overloads the `+` operator)
- `Polynomial.__sub__` – subtracts two polynomials (overloads the binary `-` operator)
- `Polynomial.__mul__` – multiplies two polynomials (overloads the `*` operator)
- `Polynomial.__truediv__` – divides two polynomials (overloads the `/` operator)
- `Polynomial.__floordiv__` – returns the quotient of dividing two polynomials (overloads the `//` operator)
- `Polynomial.__mod__` – returns the remainder of dividing two polynomials (overloads the `%` operator)

Please use the template `tasks/polynomial.py` for the implementation
and refer to the sample tests `tests/test_polynomial.py` to see some examples.
