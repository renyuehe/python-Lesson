class HookMethodClass(object):
    def __init__(self):
        self.hook_method = None

    def register_method_hook(self, method):
        self.hook_method = method

    def play(self):
        if self.hook_method == None:
            print("未接受到注册方法")
        else:
            print("接受到了方法")
            self.hook_method()


def hooked_method():
    print("我是一个业务方法，需要注册使用")

# 钩子函数就是回调函数,卧槽真尼玛会取名字
# 这个到底是 钩子 还是 回调 有待考证
if __name__ == "__main__":
    pass
    hooka = HookMethodClass()
    hooka.register_method_hook(hooked_method)
    hooka.play()