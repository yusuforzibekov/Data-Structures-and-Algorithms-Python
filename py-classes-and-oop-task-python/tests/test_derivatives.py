"""Sample tests for programming assignment: Functions and derivatives"""
import math
import pytest
from tasks.derivatives import *


def test_constant_value():
    c = C(1)
    assert c(0) == pytest.approx(1)
    assert c(1) == pytest.approx(1)


def test_constant_derivative():
    c = C(1)
    d = c.derivative()
    assert d(0) == pytest.approx(0)
    assert d(1) == pytest.approx(0)
    assert d(-100) == pytest.approx(0)


def test_power_values():
    p = Power(2)
    assert p(1) == pytest.approx(1)
    assert p(2) == pytest.approx(4)
    assert p(-3) == pytest.approx(9)

    p = Power(1)
    assert p(1) == pytest.approx(1)
    assert p(2) == pytest.approx(2)
    assert p(-3) == pytest.approx(-3)

    p = Power(0)
    assert p(1) == pytest.approx(1)
    assert p(2) == pytest.approx(1)
    assert p(-100) == pytest.approx(1)

    p = Power(-1)
    assert p(2) == pytest.approx(0.5)
    assert p(5) == pytest.approx(0.2)


def test_power_derivative():
    d = Power(2).derivative()
    assert d(1) == pytest.approx(2)
    assert d(2) == pytest.approx(4)
    assert d(-3) == pytest.approx(-6)

    d = Power(1).derivative()
    assert d(1) == pytest.approx(1)
    assert d(2) == pytest.approx(1)
    assert d(-3) == pytest.approx(1)

    d = Power(0).derivative()
    assert d(1) == pytest.approx(0)
    assert d(2) == pytest.approx(0)
    assert d(-100) == pytest.approx(0)

    d = Power(-1).derivative()
    assert d(2) == pytest.approx(-0.25)
    assert d(5) == pytest.approx(-0.04)


def test_sin_values():
    sin = Sin()
    assert sin(math.pi / 6) == pytest.approx(0.5)
    assert sin(0) == pytest.approx(0)
    assert sin(math.pi / 2) == pytest.approx(1)


def test_sin_derivative():
    cos = Sin().derivative()
    assert cos(math.pi / 3) == pytest.approx(0.5)
    assert cos(0) == pytest.approx(1)
    assert cos(math.pi / 2) == pytest.approx(0)


def test_cos_values():
    cos = Cos()
    assert cos(math.pi / 3) == pytest.approx(0.5)
    assert cos(0) == pytest.approx(1)
    assert cos(math.pi / 2) == pytest.approx(0)


def test_cos_derivative():
    neg_sin = Cos().derivative()
    assert neg_sin(math.pi / 6) == pytest.approx(-0.5)
    assert neg_sin(0) == pytest.approx(0)
    assert neg_sin(math.pi / 2) == pytest.approx(-1)


def test_exp_values():
    e = Exp()
    assert e(0) == pytest.approx(1)
    assert e(1) == pytest.approx(math.e)
    assert e(-2) == pytest.approx(math.e ** (-2))

    a = Exp(2)
    assert a(0) == pytest.approx(1)
    assert a(2) == pytest.approx(4)
    assert a(4) == pytest.approx(16)
    assert a(-2) == pytest.approx(0.25)


def test_exp_derivative():
    d = Exp().derivative()
    assert d(0) == pytest.approx(1)
    assert d(1) == pytest.approx(math.e)
    assert d(-2) == pytest.approx(math.e ** (-2))
    assert d(5) == pytest.approx(math.e ** 5)

    d = Exp(2).derivative()
    assert d(0) == pytest.approx(1 * math.log(2))
    assert d(2) == pytest.approx(4 * math.log(2))
    assert d(4) == pytest.approx(16 * math.log(2))
    assert d(-2) == pytest.approx(0.25 * math.log(2))


def test_log_values():
    log = Log()
    assert log(1) == pytest.approx(0)
    assert log(math.e) == pytest.approx(1)
    assert log(2) == pytest.approx(math.log(2))

    log = Log(2)
    assert log(1) == pytest.approx(0)
    assert log(0.25) == pytest.approx(-2)
    assert log(32) == pytest.approx(5)
    assert log(0.125) == pytest.approx(-3)


def test_log_derivative():
    d = Log().derivative()
    assert d(1) == pytest.approx(1)
    assert d(2) == pytest.approx(0.5)
    assert d(-2) == pytest.approx(-0.5)
    assert d(5) == pytest.approx(0.2)

    d = Log(2).derivative()
    assert d(1) == pytest.approx(1 / math.log(2))
    assert d(2) == pytest.approx(1 / (2 * math.log(2)))
    assert d(4) == pytest.approx(1 / (4 * math.log(2)))


def test_sum_value():
    f = Sum(Power(2), Power(4))
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(2)
    assert f(2) == pytest.approx(20)
    assert f(-3) == pytest.approx(90)

    f = Sum(Sin(), Cos())
    assert f(0) == pytest.approx(1)
    assert f(math.pi / 2) == pytest.approx(1)
    assert f(-math.pi / 4) == pytest.approx(0)
    assert f(2 * math.pi / 3) == pytest.approx(0.75 ** 0.5 - 0.5)


def test_sum_derivative():
    f = Sum(Power(2), Power(4)).derivative()
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(6)
    assert f(2) == pytest.approx(36)
    assert f(-3) == pytest.approx(-114)

    f = Sum(Sin(), Cos()).derivative()
    assert f(0) == pytest.approx(1)
    assert f(math.pi / 2) == pytest.approx(-1)
    assert f(-math.pi / 4) == pytest.approx(2 ** 0.5)
    assert f(2 * math.pi / 3) == pytest.approx(-0.75 ** 0.5 - 0.5)


def test_sub_value():
    f = Sub(Power(2), Power(4))
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(0)
    assert f(2) == pytest.approx(-12)
    assert f(-3) == pytest.approx(-72)

    f = Sub(Sin(), Cos())
    assert f(0) == pytest.approx(-1)
    assert f(math.pi / 2) == pytest.approx(1)
    assert f(-math.pi / 4) == pytest.approx(-(2 ** 0.5))
    assert f(2 * math.pi / 3) == pytest.approx(0.75 ** 0.5 + 0.5)


def test_sub_derivative():
    f = Sub(Power(2), Power(4)).derivative()
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(-2)
    assert f(2) == pytest.approx(-28)
    assert f(-3) == pytest.approx(102)

    f = Sub(Sin(), Cos()).derivative()
    assert f(0) == pytest.approx(1)
    assert f(math.pi / 2) == pytest.approx(1)
    assert f(-math.pi / 4) == pytest.approx(0)
    assert f(2 * math.pi / 3) == pytest.approx(0.75 ** 0.5 - 0.5)


def test_mul_value():
    f = Mul(C(3), Power(2))
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(3)
    assert f(2) == pytest.approx(12)
    assert f(-3) == pytest.approx(27)

    f = Mul(Sin(), Cos())
    assert f(0) == pytest.approx(0)
    assert f(math.pi / 2) == pytest.approx(0)
    assert f(-math.pi / 4) == pytest.approx(-0.5)
    assert f(2 * math.pi / 3) == pytest.approx(-(3 ** 0.5) / 4)


def test_mul_derivative():
    f = Mul(C(3), Power(2)).derivative()
    assert f(0) == pytest.approx(0)
    assert f(1) == pytest.approx(6)
    assert f(2) == pytest.approx(12)
    assert f(-3) == pytest.approx(-18)

    f = Mul(Sin(), Cos()).derivative()
    assert f(0) == pytest.approx(1)
    assert f(math.pi / 2) == pytest.approx(-1)
    assert f(-math.pi / 4) == pytest.approx(0)
    assert f(2 * math.pi / 3) == pytest.approx(-0.5)


def test_div_value():
    f = Div(C(1), Power(2))
    assert f(1) == pytest.approx(1)
    assert f(2) == pytest.approx(0.25)
    assert f(-4) == pytest.approx(0.0625)

    f = Div(Sin(), Cos())
    assert f(0) == pytest.approx(0)
    assert f(-math.pi / 4) == pytest.approx(-1)
    assert f(math.pi / 3) == pytest.approx(3 ** 0.5)


def test_div_derivative():
    f = Div(C(1), Power(2)).derivative()
    assert f(1) == pytest.approx(-2)
    assert f(2) == pytest.approx(-0.25)
    assert f(-4) == pytest.approx(0.03125)

    f = Div(Sin(), Cos()).derivative()
    assert f(0) == pytest.approx(1)
    assert f(-math.pi / 4) == pytest.approx(2)
    assert f(math.pi / 3) == pytest.approx(4)


def test_composition_value():
    f = Comp(Power(2), Cos())
    assert f(0) == pytest.approx(1)
    assert f(math.pi / 2) == pytest.approx(0)
    assert f(math.pi / 4) == pytest.approx(0.5)
    assert f(-2 * math.pi / 3) == pytest.approx(0.25)


def test_composition_derivative():
    f = Comp(Power(2), Cos()).derivative()
    assert f(0) == pytest.approx(0)
    assert f(math.pi / 2) == pytest.approx(0)
    assert f(math.pi / 4) == pytest.approx(-1)
    assert f(-2 * math.pi / 3) == pytest.approx(-(0.75 ** 0.5))
