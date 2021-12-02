import ast

name = "123123"

'''
安全地计算表达式节点或包含Python的字符串  
表达式。 提供的字符串或节点只能包含以下内容  
Python文字结构:字符串、字节、数字、元组、列表、字典、  
集合、布尔值和None。  
'''
ret = ast.literal_eval(name)
print(ret)