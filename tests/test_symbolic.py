import sympy as sp
import pytest
from mathematica_x.symbolic import differentiate, integrate

def test_differentiate():
    x = sp.Symbol("x")
    assert sp.simplify(differentiate("x**3 + 2*x") - (3*x**2+2)) == 0

def test_integrate():
    x = sp.Symbol("x")
    assert sp.diff(integrate("x**2"), x) == x**2

def test_trigonometric_identity_and_constants():
    assert sp.simplify(differentiate("sin(x)**2 + cos(x)**2")) == 0
    assert differentiate("sin(t) + pi", "t") == sp.cos(sp.Symbol("t"))

def test_rejects_unsafe_syntax():
    with pytest.raises(ValueError): differentiate("__import__('os')")

def test_rejects_invalid_variable():
    with pytest.raises(ValueError): differentiate("x", "x+y")
