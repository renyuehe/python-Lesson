'''
即实际python代码的处理过程如下：

源代码解析 --> 语法树 --> 抽象语法树(AST) --> 控制流程图 --> 字节码


大部分时间编程可能都不需要用到抽象语法树，但是在特定的条件和需求的情况下，AST又有其特殊的方便性。

下面是一个抽象语法的简单实例。
'''

func_def = \
    """ 
    def add(x, y):
        return x+y
    
    print(add(3,5))
    """
print(func_def)


def add(x, y):
    return x + y

print(add(3, 5))