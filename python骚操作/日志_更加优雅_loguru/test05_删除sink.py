from loguru import logger

trace = logger.add('runtime.log')
logger.debug('this is a debug message')
logger.remove(trace)
logger.debug('this is another debug message')


'''
删除 sink
另外添加 sink 之后我们也可以对其进行删除，相当于重新刷新并写入新的内容。 删除的时候根据刚刚 add 方法返回的 id 进行删除即可，看下面的例子：

看这里，我们首先 add 了一个 sink，然后获取它的返回值，赋值为 trace。
随后输出了一条日志，然后将 trace 变量传给 remove 方法，再次输出一条日志，
看看结果是怎样的。 控制台输出如下：

日志文件 runtime.log 内容如下：
2019-10-13 23:18:26.469 | DEBUG    | __main__:<module>:4 - this is a debug message

可以发现，在调用 remove 方法之后，确实将历史 log 删除了。
但实际上这并不是删除，只不过是将 sink 对象移除之后，在这之前的内容不会再输出到日志中。 
这样我们就可以实现日志的刷新重新写入操作。
'''