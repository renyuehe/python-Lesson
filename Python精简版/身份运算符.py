a = 1
b = 1
print(a is b)

print("======================================")


class Animal:
    pass


class Cat(Animal):
    pass


class Desk:
    pass


c = Cat()
d = Desk()
e = Animal()
print(c is e)
print(d is e)
print(d is c)
