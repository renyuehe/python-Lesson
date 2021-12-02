
import ast
import astunparse

func_def = \
    """ 
def add(x, y):
    return x+y

print(add(3,5))
    """

class CodeTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node) # 这里表示先去访问里面的children node
        if node.name == 'add':
            node.name = 'sub'
        args_num = len(node.args.args)

        args_num = len(node.args.args)
        args = tuple([arg.arg for arg in node.args.args])
        print(str(args))
        func_log_stmt = ''.join(["print('calling func: %s', " % node.name, "'args:'", ", %s" * args_num % args ,')'])
        node.body.insert(0, ast.parse(func_log_stmt))

        # func_log_stmt = ''.join(["print 'calling func: %s', " % node.name, "'args:'", ", %s" * args_num % args])
        # node.body.insert(0, ast.parse(func_log_stmt))

        return node

    def visit_Name(self, node):
        replace = {'add': 'sub', 'x': 'a', 'y': 'b'}
        re_id = replace.get(node.id, None)
        node.id = re_id or node.id
        self.generic_visit(node)
        return node

    def visit_arg(self, node):
        self.generic_visit(node)
        replace = {'x': 'a', 'y': 'b'}
        node.arg = replace[node.arg]
        return node



r_node = ast.parse(func_def)
transformer = CodeTransformer()
r_node = transformer.visit(r_node)
# print(astunparse.dump(r_node))
source = astunparse.unparse(r_node)  # astunparse 一般python不自带，需要conda 或者 pip安装
print(source)