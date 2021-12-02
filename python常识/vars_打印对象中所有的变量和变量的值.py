
class Base():
    def __init__(self):
        self.a = 10

class Child(Base):
    def __init__(self):
        super(Child, self).__init__() # 加了就有 a ，不加就没 a
        
        self.b = 11
        self.c = "gggg"
        self.d = {1:"one"}

child = Child()

print(vars(child))