class Person:

    def __init__(self, name):
        self.name = name
        self.height = 1.72
        self.sex = "男"

    def show(self):
        print(self.name)
        #self.height = 1.78
        print(self.height)
        print(self.sex)

p = Person("张三")
p.show()

p.height = 1.75
print(p.height)
