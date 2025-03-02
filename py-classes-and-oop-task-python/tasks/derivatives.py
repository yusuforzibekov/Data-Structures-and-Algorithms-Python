"""Solution for programming assignment: Functions and derivatives"""
import math
from abc import ABC


# Abstract classes for functions and operators

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


# Classes implementing binary operators

class Sum(BinaryOperator):
    """Class for the sum of two arguments: f(x) + g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) + self.right(x)

    def derivative(self) -> Function:
        return Sum(self.left.derivative(), self.right.derivative())


class Sub(BinaryOperator):
    """Class for the subtraction of two arguments: f(x) - g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) - self.right(x)

    def derivative(self) -> Function:
        return Sub(self.left.derivative(), self.right.derivative())


class Mul(BinaryOperator):
    """Class for the multiplication of two arguments: f(x) * g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) * self.right(x)

    def derivative(self) -> Function:
        return Sum(Mul(self.left.derivative(), self.right), Mul(self.left, self.right.derivative()))


class Div(BinaryOperator):
    """Class for the division of two arguments: f(x) / g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) / self.right(x)

    def derivative(self) -> Function:
        return Div(Sub(Mul(self.left.derivative(), self.right), Mul(self.left, self.right.derivative())), Mul(self.right, self.right))


class Comp(BinaryOperator):
    """Class for the composition of two arguments: f(g(x))"""
    def __call__(self, x: float) -> float:
        return self.left(self.right(x))

    def derivative(self) -> Function:
        return Mul(Comp(self.left.derivative(), self.right), self.right.derivative())


# Classes implementing elementary functions

class C(Function):
    """Class for constant function: C(x) = c for all x"""
    def __init__(self, c: float):
        self.c = c

    def __call__(self, x: float) -> float:
        return self.c

    def derivative(self) -> Function:
        return C(0)


class Power(Function):
    """
    Class for power function: P(x) = x^n.
    Defaults to the identity function.
    """
    def __init__(self, n: float = 1):
        self.n = n

    def __call__(self, x: float) -> float:
        return x ** self.n

    def derivative(self) -> Function:
        return Mul(C(self.n), Power(self.n - 1))


class Sin(Function):
    """
    Class for sinus function.
    HINT: use `math` package to compute the value of
    the function at some point
    """
    def __call__(self, x: float) -> float:
        return math.sin(x)

    def derivative(self) -> Function:
        return Cos()


class Cos(Function):
    """
    Class for cosine function
    HINT: use `math` package to compute the value of
    the function at some point
    """
    def __call__(self, x: float) -> float:
        return math.cos(x)

    def derivative(self) -> Function:
        return Mul(C(-1), Sin())


class Exp(Function):
    """
    Class for exponent function: E(x) = a^x, where a is a fixed base.
    Defaults to the natural exponent e^x.
    HINT: use `math` package to compute the value of
    the function at some point
    """
    def __init__(self, base: float = math.e):
        self.base = base

    def __call__(self, x: float) -> float:
        return self.base ** x

    def derivative(self) -> Function:
        return Mul(C(math.log(self.base)), Exp(self.base))


class Log(Function):
    """
    Class for the logarithm with a fixed base a: L(x) = log_a(x).
    Defaults to the natural logarithm ln(x).
    HINT: use `math` package to compute the value of
    the function at some point
    """
    def __init__(self, base: float = math.e):
        self.base = base

    def __call__(self, x: float) -> float:
        return math.log(x, self.base)

    def derivative(self) -> Function:
        return LogDerivative(self.base)


class LogDerivative(Function):
    def __init__(self, base):
        self.base = base

    def __call__(self, x):
        return 1 / (x * math.log(self.base))


class FloorDiv(BinaryOperator):
    """Class for the floor division of two arguments: f(x) // g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) // self.right(x)

    def derivative(self) -> Function:
        # The derivative of floor division is complex and often zero, so we return a constant zero function.
        return C(0)


class Mod(BinaryOperator):
    """Class for the modulo of two arguments: f(x) % g(x)"""
    def __call__(self, x: float) -> float:
        return self.left(x) % self.right(x)

    def derivative(self) -> Function:
        # The derivative of modulo is complex and often discontinuous, so we return a constant zero function.
        return C(0)
