import sympy as sp
from mathematica_x.symbolic import differentiate, integrate

def test_differentiate():
    assert sp.simplify(differentiate("x**3 + 2*x") - (3*sp.Symbol("x")**2+2)) == 0

def test_integrate():
    assert sp.diff(integrate("x**2"), sp.Symbol("x")) == sp.Symbol("x")**2
