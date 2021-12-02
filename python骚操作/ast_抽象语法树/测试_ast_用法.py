import ast

def test02():
    node = ast.UnaryOp()
    node.op = ast.USub()
    node.operand = ast.Num()
    node.operand.n = 5
    node.operand.lineno = 0
    node.operand.col_offset = 0
    node.lineno = 0
    node.col_offset = 0

    print(node)
    print(node.op)
    print(node.operand)
    print(node.operand.n)
    print(node.operand.lineno)
    print(node.operand.col_offset)
    print(node.lineno)
    print(node.col_offset)

def test01():
    node = ast.UnaryOp(ast.USub(), ast.Num(5, lineno=0, col_offset=0),
                       lineno=0, col_offset=0)
    print(node)
    print(node.op)
    print(node.operand)
    print(node.operand.n)
    print(node.operand.lineno)
    print(node.operand.col_offset)
    print(node.lineno)
    print(node.col_offset)

test01()
# test02()
