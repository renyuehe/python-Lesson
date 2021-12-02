import ast

func_def = \
    """ 
def add(x, y):
    return x+y

print(add(3,5))
    """

cm1 = ast.parse(func_def,filename='<unknown>', mode='exec')

print(type(cm1))

# print(ast.dump(cm1))

import pprint
pprint.pprint(ast.dump(cm1))