class Man:          # object
    def __new__(cls, *args, **kwargs):
        print("new方法被执行。。。")           # 增加功能的操作
        # 调用object的new方法
        instance = object.__new__(Man)         # 分配一个内存空间
                                               # instance这是一个变量此处老师建议必须使用该单词
        return instance                        # instance 中义：实例对象
    def __init__(self, name, age):
        print("init方法被执行。。。")
        self.name = name
        self.age = age
man1 = Man("小明", 18)