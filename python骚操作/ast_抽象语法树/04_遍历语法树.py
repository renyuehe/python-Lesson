

'''
3. 遍历语法树
python提供了两种方式来遍历整个语法树

节点的访问就只需要重写 visit_nodename函数，在里面定义参数即可
这里节点的visit 会默认根据 ast中的 nodename 去访问 visit_nodename 函数，同时如果当前节点存- 在children，比如 FunctionDef 中存在 BinOp 节点，若想 visit BinOp这个节点，就需要在 FunctionDef中增加一句 self.generic_visit()来达到递归访问；如果不加，就只能访问当前节点
generic_visit(node)
'''

import ast

func_def = \
    """ 
def add(x, y):
    return x+y

print(add(3,5))
    """


'''
ast.NodeVisitor
'''
class CodeVisitor(ast.NodeVisitor):
    def visit_BinOp(self, node):  # 这个函数的访问是由于 Visit_FunctionDef的先访问再generic_visit才访问的
        print('Bin')  # 如果Visit_FunctionDef中没有generic_visit的话，则这个函数是不会访问的
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        print('Function Name: %s' % node.name)
        self.generic_visit(node)  # FunctionDef中还包含有 BinOp,因此会进去visit BinOP

    def visit_Call(self, node):
        print("call")
        self.generic_visit(node)  # 因为AST的Call中还包含有一个Call,因此会重复再访问一次


r_node = ast.parse(func_def)
visitor = CodeVisitor()
visitor.visit(r_node)  # 这里的visit函数会根据 node 的语法树去遍历里面的函数，
