class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)


cat1 = Cat("大白")
cat1.show()
