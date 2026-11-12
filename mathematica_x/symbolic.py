"""Symbolic operations powered by SymPy."""
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy import sin, cos, tan, exp, log, sqrt, pi, E

def _parse(expression):
    x = sp.Symbol("x")
    allowed = {"x": x, "sin": sin, "cos": cos, "tan": tan, "exp": exp,
               "log": log, "sqrt": sqrt, "pi": pi, "E": E}
    return parse_expr(expression, local_dict=allowed, global_dict={"__builtins__": {}}, evaluate=True)

def differentiate(expression, variable="x"):
    symbol = sp.Symbol(variable)
    return sp.diff(_parse(expression), symbol)

def integrate(expression, variable="x"):
    symbol = sp.Symbol(variable)
    return sp.integrate(_parse(expression), symbol)
