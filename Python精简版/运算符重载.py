class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age


zhang3 = Person("张三", 32)
li4 = Person("李四", 36)
print(zhang3 + li4)  # 张三和李4的总年龄为68岁
