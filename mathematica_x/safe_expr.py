"""Small, restricted expression evaluator for numerical functions."""
import ast
import math
import operator

_ALLOWED = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}
_FUNCTIONS = {name: getattr(math, name) for name in
              ("sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log", "log10", "exp", "fabs")}
_FUNCTIONS.update({"abs": abs})
_CONSTANTS = {"pi": math.pi, "e": math.e}

def compile_expression(expression):
    """Compile a mathematical expression into a callable f(x)."""
    tree = ast.parse(expression, mode="eval")
    def visit(node, x):
        if isinstance(node, ast.Expression): return visit(node.body, x)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)): return node.value
        if isinstance(node, ast.Name):
            if node.id == "x": return x
            if node.id in _CONSTANTS: return _CONSTANTS[node.id]
            raise ValueError(f"Unknown symbol: {node.id}")
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](visit(node.left, x), visit(node.right, x))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
            return _ALLOWED[type(node.op)](visit(node.operand, x))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCTIONS:
            if len(node.args) != 1: raise ValueError("Functions take exactly one argument.")
            return _FUNCTIONS[node.func.id](visit(node.args[0], x))
        raise ValueError("Unsupported expression. Use x, arithmetic, and standard math functions.")
    return lambda x: float(visit(tree, float(x)))
