class Foo(object):
    def __init__(self, key, value):
        self.key = []
        self.value = []
        self.key.append(key)
        self.value.append(value)
        self.__index = 0

    def __len__(self):
        return len(self.key)

    def __str__(self):
        return str("__str__ print")

    def __myfun__(self):
        print("__myfun__ print")

f = Foo(1, 2)
f.__myfun__()
print(f)
