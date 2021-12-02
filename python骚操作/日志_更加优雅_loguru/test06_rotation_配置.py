''''''
'''
用了 loguru 我们还可以非常方便地使用 rotation 配置，比如我们想一天输出一个日志文件，或者文件太大了自动分隔日志文件，
我们可以直接使用 add 方法的 rotation 参数进行配置。 我们看看下面的例子：

logger.add('runtime_{time}.log', rotation="500 MB")

通过这样的配置我们就可以实现每 500MB 存储一个文件，每个 log 文件过大就会新创建一个 log 文件。
我们在配置 log 名字时加上了一个 time 占位符，这样在生成时可以自动将时间替换进去，生成一个文件名包含时间的 log 文件。 
另外我们也可以使用 rotation 参数实现定时创建 log 文件，例如：

logger.add('runtime_{time}.log', rotation='00:00')

这样就可以实现每天 0 点新创建一个 log 文件输出了。 
另外我们也可以配置 log 文件的循环时间，比如每隔一周创建一个 log 文件，写法如下：

logger.add('runtime_{time}.log', rotation='1 week')

这样我们就可以实现一周创建一个 log 文件了。
'''