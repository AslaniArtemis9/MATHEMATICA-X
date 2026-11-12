import math
import pytest
from mathematica_x.numerical import derivative, simpson, bisection, newton

def test_derivative(): assert derivative("x**2", 3) == pytest.approx(6, rel=1e-6)
def test_simpson(): assert simpson("sin(x)", 0, math.pi, 100) == pytest.approx(2, rel=1e-8)
def test_simpson_odd_intervals_are_adjusted(): assert simpson("x", 0, 1, 3) == pytest.approx(0.5)
def test_bisection(): assert bisection("x**2-2", 0, 2) == pytest.approx(math.sqrt(2), rel=1e-8)
def test_bisection_endpoint_root(): assert bisection("x", 0, 2) == 0
def test_newton(): assert newton("x**2-2", 1.0) == pytest.approx(math.sqrt(2), rel=1e-8)
def test_rejects_unbracketed_root():
    with pytest.raises(ValueError): bisection("x**2+1", -1, 1)
def test_rejects_invalid_simpson_count():
    with pytest.raises(ValueError): simpson("x", 0, 1, 0)
def test_rejects_unsafe_expression():
    with pytest.raises(ValueError): derivative("__import__('os')", 1)
