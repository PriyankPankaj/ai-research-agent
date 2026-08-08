from src.tools.base import BaseTool
import ast
import operator


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a basic arithmetic expression, e.g. '12 * (4 + 3)'."

    _OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }

    def _eval(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            return self._OPS[type(node.op)](self._eval(node.left), self._eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return self._OPS[type(node.op)](self._eval(node.operand))
        else:
            raise ValueError("Unsupported expression")

    def run(self, input_text: str) -> str:
        try:
            tree = ast.parse(input_text, mode="eval")
            result = self._eval(tree.body)
            return str(result)
        except Exception as e:
            return f"Calculator error: could not evaluate '{input_text}' ({str(e)})"