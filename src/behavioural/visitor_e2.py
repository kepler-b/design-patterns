"""
Incomplete Implementation

def _visitor_impl(self, arg):
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)
def visitor(arg_type):
    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn
        return _visitor_impl
"""
class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)

class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visit(self)

class ExpressionPrinter:
    def __init__(self) -> None:
        self.buffer = []

    def visit(self, de):
        self.buffer.append(str(de.value))

    def visit(self, ae):
        self.buffer.append("(")
        ae.left.accept(self)
        self.buffer.append("+")
        ae.right.accept(self)
        self.buffer.append(")")

    def __str__(self):
        return "".join(self.buffer)

def execute():
    e = AdditionExpression(DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
    print(e)
