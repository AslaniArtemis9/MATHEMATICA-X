"""Numerical differentiation, integration and root finding."""
from .safe_expr import compile_expression

def derivative(expression, x, h=1e-5):
    f = compile_expression(expression)
    return (f(x + h) - f(x - h)) / (2 * h)

def simpson(expression, a, b, n=200):
    if n <= 0: raise ValueError("n must be positive")
    if n % 2: n += 1
    f = compile_expression(expression)
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4 * sum(f(a + i*h) for i in range(1, n, 2))
    total += 2 * sum(f(a + i*h) for i in range(2, n, 2))
    return total * h / 3

def bisection(expression, a, b, tolerance=1e-10, max_iterations=200):
    f = compile_expression(expression)
    fa, fb = f(a), f(b)
    if fa * fb > 0: raise ValueError("The interval must bracket a root.")
    for _ in range(max_iterations):
        mid = (a + b) / 2
        fm = f(mid)
        if abs(fm) < tolerance or abs(b-a) / 2 < tolerance: return mid
        if fa * fm <= 0: b, fb = mid, fm
        else: a, fa = mid, fm
    raise RuntimeError("Bisection did not converge.")

def newton(expression, x0, tolerance=1e-10, max_iterations=100):
    f = compile_expression(expression)
    x = float(x0)
    for _ in range(max_iterations):
        slope = derivative(expression, x)
        if abs(slope) < 1e-14: raise ZeroDivisionError("Derivative is too close to zero.")
        nxt = x - f(x) / slope
        if abs(nxt-x) < tolerance: return nxt
        x = nxt
    raise RuntimeError("Newton's method did not converge.")
