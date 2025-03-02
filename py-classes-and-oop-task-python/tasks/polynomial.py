"""Template for programming assignment: Polynomials"""
from itertools import zip_longest
from typing import Optional, Tuple


class Polynomial:
    """
    Class that implements basic operations over polynomials:
    P(x) = c_n x^n + ... + c_1 x + c_0.
    Note that the polynomial function is fully determined by its
    coefficients (c_n, ..., c_1, c_0).
    """
    def __init__(self, *coefficients: float):
        """
        Args:
            coefficients: list of numbers
                The coefficients of the polynomials in the order
                of descending degrees: for example, the polynomial
                x^2 + 2 x + 3 should correspond to Polynomial(1, 2, 3).
        """
        self.__coefficients = list(coefficients)
        self.trim()

    def trim(self):
        """
        Removes leading zeros from the array of coefficients, so that
        polynomials 0 x^3 + 2 x^2 + 1 and 2 x^2 + 1 are equivalent.
        NOTE: to check if a coefficient is zero, please compare its
        absolute value with 1e-6.
        """
        while self.__coefficients and abs(self.__coefficients[0]) < 1e-6:
            self.__coefficients.pop(0)
        if not self.__coefficients:
            self.__coefficients = [0.0]

    def degree(self) -> Optional[int]:
        """
        Degree of the polynomial, i.e. the largest degree of its monomials.
        NOTE: the degree of the zero polynomial P(x) = 0 must be None.
        """
        if not self.__coefficients or (len(self.__coefficients) == 1 and abs(self.__coefficients[0]) < 1e-6):
            return None
        return len(self.__coefficients) - 1

    def __call__(self, x: float) -> float:
        """
        Calculates the value of the polynomial at point x.

        Args:
            x: float, point to be substituted into the polynomial
        Returns:
            float, the value of the polynomial at point x
        """
        result = 0
        for i, coeff in enumerate(reversed(self.__coefficients)):
            result += coeff * (x ** i)
        return result

    def __add__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Calculates the sum of two polynomials.
        HINT: you might find helpful the `zip_longest` method from
        `itertools` package, it is already imported for you.

        Args:
            other: Polynomial, the polynomial to be added to this polynomial.
        Returns:
            Polynomial, the sum of this polynomial and the `other` one.
        """
        new_coefficients = [x + y for x, y in zip_longest(self.__coefficients[::-1], other.__coefficients[::-1], fillvalue=0)][::-1]
        return Polynomial(*new_coefficients)

    def __neg__(self) -> 'Polynomial':
        """Calculates the negated polynomial, i.e. the
        polynomial multiplied by -1"""
        return Polynomial(*[-c for c in self.__coefficients])

    def __sub__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Calculates the subtraction of two polynomials.
        HINT: you might find helpful the negation operator declared above.

        Args:
            other: Polynomial,
                the polynomial to be subtracted from this polynomial.
        Returns:
            Polynomial, the difference between this polynomial and
            the `other` one.
        """
        return self + (-other)

    def __mul__(self, other: 'Polynomial') -> 'Polynomial':
        """
        Calculates the multiplication of two polynomials
        HINT: you might find helpful the "+=" operator already implemented
        for you (based on your implementation of the "+" operator)

        Args:
            other: Polynomial,
                the polynomial to be multiplied with this polynomial.
        Returns:
            Polynomial, the product of this polynomial and the `other` one.
        """
        if self.degree() is None or other.degree() is None:
            return Polynomial(0.0)

        result_coeffs = [0.0] * (self.degree() + other.degree() + 1)
        for i, self_coeff in enumerate(self.__coefficients):
            for j, other_coeff in enumerate(other.__coefficients):
                result_coeffs[i + j] += self_coeff * other_coeff
        return Polynomial(*result_coeffs)

    def __truediv__(self, other: 'Polynomial') -> Tuple['Polynomial', 'Polynomial']:
        if other.degree() is None:
            raise ZeroDivisionError("Cannot divide by zero polynomial")

        if self.degree() is None:
            return Polynomial(0), Polynomial(0)
            
        if self.degree() < other.degree():
            return Polynomial(0), Polynomial(*self.__coefficients)

        quotient_coeffs = [0] * (self.degree() - other.degree() + 1)
        remainder = list(self.__coefficients)

        for i in range(len(quotient_coeffs)):
            if abs(remainder[0]) < 1e-6:
                remainder.pop(0)
                continue
                
            # Calculate the coefficient for the quotient
            coeff = remainder[0] / other.__coefficients[0]
            quotient_coeffs[i] = coeff
            
            # Subtract (divisor * coeff * x^k) from the remainder
            for j in range(len(other.__coefficients)):
                if j < len(remainder):
                    remainder[j] -= coeff * other.__coefficients[j]
            
            # Remove the leading term
            remainder.pop(0)

        # Create polynomials from the results
        quotient = Polynomial(*quotient_coeffs)
        remainder = Polynomial(*remainder) if remainder else Polynomial(0)
        
        return quotient, remainder

    def __floordiv__(self, other):
        """
        Calculates the quotient of the division of two polynomials

        Args:
            other: Polynomial,
                the polynomial by which this polynomial is to be divided.
        Returns:
            Polynomial,
                The quotient of the division of this polynomial
                by the `other` one.
        """
        return self.__truediv__(other)[0]

    def __mod__(self, other):
        """
        Calculates the remainder of the division of two polynomials

        Args:
            other: Polynomial,
                the polynomial by which this polynomial is to be divided.
        Returns:
            Polynomial,
                The remainder of the division of this polynomial
                by the `other` one.
        """
        return self.__truediv__(other)[1]

    def __iadd__(self, other: 'Polynomial') -> 'Polynomial':
        return self + other

    def __isub__(self, other: 'Polynomial') -> 'Polynomial':
        return self - other

    def __eq__(self, other):
        """Checks if two polynomials are equal"""
        if self.degree() != other.degree():
            return False

        return all([
            abs(x - y) < 1e-6 if isinstance(x, float) or isinstance(y, float)
            else x == y
            for x, y in zip(self.__coefficients, other.__coefficients)
        ])

    def __repr__(self) -> str:
        return f'Polynomial({", ".join([str(c) for c in self.__coefficients])})'
