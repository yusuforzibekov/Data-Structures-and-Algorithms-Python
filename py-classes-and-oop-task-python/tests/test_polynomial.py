"""Sample tests for programming assignment: Polynomials"""
from tasks.polynomial import Polynomial


def test_trim():
    assert Polynomial(0, 0, 2, 1) == Polynomial(2, 1)
    assert Polynomial(1) == Polynomial(1)


def test_degree():
    assert Polynomial(1).degree() == 0
    assert Polynomial(1, 2, 1).degree() == 2
    assert Polynomial(0).degree() is None


def test_call():
    p = Polynomial(1, 2, 3)
    assert p(1) == 6
    assert p(-2) == 3

    p = Polynomial(1)
    assert p(0) == 1
    assert p(1) == 1
    assert p(-3) == 1

    p = Polynomial()
    assert p(1) == 0
    assert p(-2) == 0


def test_add():
    assert Polynomial(1, 2, 3) + Polynomial(-1, 1) == Polynomial(1, 1, 4)
    assert Polynomial(1, -1, -3) + Polynomial(3) == Polynomial(1, -1, 0)
    assert Polynomial(2, 4, -2) + Polynomial(-2, 0, 0) == Polynomial(4, -2)


def test_sub():
    assert Polynomial(1, 2, 3) - Polynomial(-1, 1) == Polynomial(1, 3, 2)
    assert Polynomial(1, -1, 3) - Polynomial(2, 0, 3) == Polynomial(-1, -1, 0)
    assert Polynomial(2, 4, -2) - Polynomial(2, 0, 0) == Polynomial(4, -2)


def test_mul():
    assert Polynomial(1, 2, 3) * Polynomial(2) == Polynomial(2, 4, 6)
    assert Polynomial(1, -1) * Polynomial(1, 2) == Polynomial(1, 1, -2)
    assert Polynomial(1, 2, 3) * Polynomial(0) == Polynomial(0)
    assert Polynomial(-3) * Polynomial(4) == Polynomial(-12)
    assert Polynomial(1, 1) * Polynomial(1, 2, 1) == Polynomial(1, 3, 3, 1)


def test_div():
    assert Polynomial(2, 4, 6) / Polynomial(2) == (Polynomial(1, 2, 3), Polynomial(0))
    assert Polynomial(-3) / Polynomial(4) == (Polynomial(-0.75), Polynomial(0))
    assert Polynomial(1, 1) / Polynomial(1, 2, 1) == (Polynomial(0), Polynomial(1, 1))
    assert Polynomial(1, 2, 3) / Polynomial(1, 1) == (Polynomial(1, 1), Polynomial(2))


def test_floordiv():
    assert Polynomial(2, 4, 6) // Polynomial(2) == Polynomial(1, 2, 3)
    assert Polynomial(-3) // Polynomial(4) == Polynomial(-0.75)
    assert Polynomial(1, 1) // Polynomial(1, 2, 1) == Polynomial(0)
    assert Polynomial(1, 2, 3) // Polynomial(1, 1) == Polynomial(1, 1)


def test_mod():
    assert Polynomial(2, 4, 6) % Polynomial(2) == Polynomial(0)
    assert Polynomial(-3) % Polynomial(4) == Polynomial(0)
    assert Polynomial(1, 1) % Polynomial(1, 2, 1) == Polynomial(1, 1)
    assert Polynomial(1, 2, 3) % Polynomial(1, 1) == Polynomial(2)
