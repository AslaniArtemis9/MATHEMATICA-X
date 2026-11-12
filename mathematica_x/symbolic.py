"""Safe symbolic operations powered by SymPy."""
import ast
import operator
import sympy as sp

_BINARY = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
           ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod}
_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}
_FUNCTIONS = {name: getattr(sp, name) for name in
              ("sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh", "exp", "log", "sqrt")}
_FUNCTIONS.update({"abs": sp.Abs})
_CONSTANTS = {"pi": sp.pi, "E": sp.E, "e": sp.E}

def _parse(expression):
    """Parse a restricted mathematical expression without eval/parse_expr."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Expression must be a non-empty string.")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid mathematical expression.") from exc
    def visit(node):
        if isinstance(node, ast.Expression): return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return sp.Integer(node.value) if isinstance(node.value, int) else sp.Float(node.value)
        if isinstance(node, ast.Name):
            if node.id in _CONSTANTS: return _CONSTANTS[node.id]
            if node.id.startswith("__"): raise ValueError("Private names are not allowed.")
            return sp.Symbol(node.id)
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY:
            return _BINARY[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
            return _UNARY[type(node.op)](visit(node.operand))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCTIONS:
            if node.keywords or len(node.args) != 1:
                raise ValueError("Mathematical functions require exactly one positional argument.")
            return _FUNCTIONS[node.func.id](visit(node.args[0]))
        raise ValueError("Unsupported syntax. Use variables, arithmetic, and supported math functions.")
    return visit(tree)

def _symbol(variable):
    if not isinstance(variable, str) or not variable.isidentifier() or variable.startswith("__"):
        raise ValueError("Variable must be a valid identifier.")
    return sp.Symbol(variable)

def differentiate(expression, variable="x"):
    return sp.diff(_parse(expression), _symbol(variable))

def integrate(expression, variable="x"):
    return sp.integrate(_parse(expression), _symbol(variable))
