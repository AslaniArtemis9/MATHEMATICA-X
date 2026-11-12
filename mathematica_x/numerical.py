"""Numerical differentiation, integration and root finding."""
import math
from .safe_expr import compile_expression

def _finite_number(value, name):
    value = float(value)
    if not math.isfinite(value): raise ValueError(f"{name} must be finite.")
    return value

def derivative(expression, x, h=1e-5):
    x, h = _finite_number(x, "x"), _finite_number(h, "h")
    if h <= 0: raise ValueError("h must be positive.")
    f = compile_expression(expression)
    return (f(x + h) - f(x - h)) / (2 * h)

def simpson(expression, a, b, n=200):
    a, b = _finite_number(a, "a"), _finite_number(b, "b")
    if isinstance(n, bool) or int(n) != n or n <= 0:
        raise ValueError("n must be a positive integer.")
    n = int(n)
    if n % 2: n += 1
    f = compile_expression(expression)
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4 * sum(f(a + i*h) for i in range(1, n, 2))
    total += 2 * sum(f(a + i*h) for i in range(2, n, 2))
    return total * h / 3

def bisection(expression, a, b, tolerance=1e-10, max_iterations=200):
    a, b = _finite_number(a, "a"), _finite_number(b, "b")
    tolerance = _finite_number(tolerance, "tolerance")
    if a >= b: raise ValueError("Require a < b.")
    if tolerance <= 0: raise ValueError("tolerance must be positive.")
    if isinstance(max_iterations, bool) or int(max_iterations) != max_iterations or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")
    f = compile_expression(expression)
    fa, fb = f(a), f(b)
    if fa == 0: return a
    if fb == 0: return b
    if (fa < 0) == (fb < 0): raise ValueError("The interval must bracket a root.")
    for _ in range(int(max_iterations)):
        mid = a + (b - a) / 2
        fm = f(mid)
        if fm == 0 or abs(b-a) / 2 <= tolerance: return mid
        if (fa < 0) != (fm < 0): b, fb = mid, fm
        else: a, fa = mid, fm
    raise RuntimeError("Bisection did not converge within max_iterations.")

def newton(expression, x0, tolerance=1e-10, max_iterations=100):
    x, tolerance = _finite_number(x0, "x0"), _finite_number(tolerance, "tolerance")
    if tolerance <= 0: raise ValueError("tolerance must be positive.")
    if isinstance(max_iterations, bool) or int(max_iterations) != max_iterations or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")
    f = compile_expression(expression)
    for _ in range(int(max_iterations)):
        fx = f(x)
        if abs(fx) <= tolerance: return x
        slope = derivative(expression, x)
        if abs(slope) < 1e-14: raise ZeroDivisionError("Derivative is too close to zero.")
        nxt = x - fx / slope
        if not math.isfinite(nxt): raise ArithmeticError("Newton iteration became non-finite.")
        if abs(nxt-x) <= tolerance and abs(f(nxt)) <= max(tolerance * 10, 1e-12):
            return nxt
        x = nxt
    raise RuntimeError("Newton's method did not converge within max_iterations.")
