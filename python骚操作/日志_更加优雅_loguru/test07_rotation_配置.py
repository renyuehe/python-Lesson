''''''

'''
很多情况下，一些非常久远的 log 对我们来说并没有什么用处了，它白白占据了一些存储空间，不清除掉就会非常浪费。
retention 这个参数可以配置日志的最长保留时间。 比如我们想要设置日志文件最长保留 10 天，可以这么来配置：

logger.add('runtime.log', retention='10 days')

这样 log 文件里面就会保留最新 10 天的 log，妈妈再也不用担心 log 沉积的问题啦。

'''
from loguru import logger

logger.add('runtime.log', retention='10 days')
