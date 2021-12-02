''' '''
'''
add 方法就相当于给 logger 添加了一个 Handler，它给我们暴露了许多参数来实现 Handler 的配置，下面我们来详细介绍下。 首先看看它的方法定义吧：


def add(
        self,
        sink,
        *,
        level=_defaults.LOGURU_LEVEL,
        format=_defaults.LOGURU_FORMAT,
        filter=_defaults.LOGURU_FILTER,
        colorize=_defaults.LOGURU_COLORIZE,
        serialize=_defaults.LOGURU_SERIALIZE,
        backtrace=_defaults.LOGURU_BACKTRACE,
        diagnose=_defaults.LOGURU_DIAGNOSE,
        enqueue=_defaults.LOGURU_ENQUEUE,
        catch=_defaults.LOGURU_CATCH,
        **kwargs
    ):
    pass

看看它的源代码，它支持这么多的参数，如 level、format、filter、color 等等，
另外我们还注意到它有个非常重要的参数 sink，
我们看看官方文档：https://loguru.readthedocs.io/en/stable/api/logger.html#sink，可以了解到通过 sink 我们可以传入多种不同的数据结构，汇总如下：

sink 可以传入一个 file 对象，例如 sys.stderr 或者 open('file.log', 'w') 都可以。
sink 可以直接传入一个 str 字符串或者 pathlib.Path 对象，其实就是代表文件路径的，如果识别到是这种类型，它会自动创建对应路径的日志文件并将日志输出进去。
sink 可以是一个方法，可以自行定义输出实现。
sink 可以是一个 logging 模块的 Handler，比如 FileHandler、StreamHandler 等等，或者上文中我们提到的 CMRESHandler 照样也是可以的，这样就可以实现自定义 Handler 的配置。
sink 还可以是一个自定义的类，具体的实现规范可以参见官方文档。
'''