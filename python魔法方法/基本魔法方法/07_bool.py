class Demo():

    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        # bool()是个 builtins 函数，但是可以重写
        return bool(self.value > 5)


obj = Demo()
obj.value = 0
if obj:
    print("yes")
else:
    print("no")

print(bool(obj))