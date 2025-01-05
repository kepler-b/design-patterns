"""
Visitor Pattern

A component (visitor) that knows how to traverse a data structure composed of (possibly related) data types.
"""

from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value) -> None:
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self): return self.value



class AdditionExpression(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self):
       return self.left.eval() + self.right.eval()

# If needed use this type not the print in the parent for OCP
class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(e.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(")")

Expression.print = lambda self, b: \
    ExpressionPrinter.print(self, b)

def execute():
    e = AdditionExpression(DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
    buffer = []
    e.print(buffer)
    print("".join(buffer), "=", e.eval())
