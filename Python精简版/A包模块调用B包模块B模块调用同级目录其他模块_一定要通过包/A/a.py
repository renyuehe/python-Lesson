import os

print(os.path.abspath(os.path.curdir)) #打印程序的执行路径

# import other_a #这样写的问题就是如果程序执行的起始路径不是这个问题,就无法导入这个模块
from A import other #这样写是ok的,因为包不管从哪个路径都可以找到

def funa():
    print("funa")

