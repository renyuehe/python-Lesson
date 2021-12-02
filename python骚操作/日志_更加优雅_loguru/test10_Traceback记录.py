''''''
'''
在很多情况下，如果遇到运行错误，而我们在打印输出 log 的时候万一不小心没有配置好 Traceback 的输出，很有可能我们就没法追踪错误所在了。 
但用了 loguru 之后，我们用它提供的装饰器就可以直接进行 Traceback 的记录，类似这样的配置即可：

我们做个测试，我们在调用时三个参数都传入 0，直接引发除以 0 的错误，看看会出现什么情况：

运行完毕之后，可以发现 log 里面就出现了 Traceback 信息，而且给我们输出了当时的变量值，真的是不能再赞了！结果如下：
'''

from loguru import logger

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


if __name__ == '__main__':
    my_function(0,0,0)