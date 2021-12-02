''''''
'''
@contextmanager
@contextmanager通过将一个函数变成生成器的方式来为普通类添加进入和退出时的处理代码，从而实现了将普通类变成一个上下文管理器。
'''

from contextlib import contextmanager

class File():
    def query(self):
        print('查询文件')

@contextmanager
def open():
    print('打开文件')
    yield File()
    print('关闭文件')

with open() as f:
    f.query()
    pass

# 结果 打开文件 查询文件 关闭文件

'''
执行流程
①with语句调用open函数 = > 
②执行open中yield之前的代码(打开文件) = > 
③执行yield语句中的代码(File()) = > 
④执行with语句中的代码(f.query) = > 
⑤执行yiled语句后的代码(关闭文件)
'''



