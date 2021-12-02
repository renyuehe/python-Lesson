''''''


'''
resource 资源模块

注意：这是个 unix, linux 独有的模块, windows下是不可以用的
'''

# This module provides basic mechanisms for measuring and controlling system resources utilized by a program.
# 该模块提供了测量和控制程序所利用的系统资源的基本机制。
import resource

print("usage stats", "=>", resource.getrusage(resource.RUSAGE_SELF))
print("max cpu", "=>", resource.getrlimit(resource.RLIMIT_CPU)) # 最大cpu数量
print("max data", "=>", resource.getrlimit(resource.RLIMIT_DATA)) #
print("max processes", "=>", resource.getrlimit(resource.RLIMIT_NPROC))
print("page size", "=>", resource.getpagesize())

'''
Resources usage can be limited using the setrlimit() function described below.
可以使用下面描述的设置限制()函数来限制资源的使用。
'''
