print('__len__' in dir(list))  # True
print('__len__' in dir(dict))  # True
print('__len__' in dir(set))   # True
print('__len__' in dir(tuple))  # True
print('__len__' in dir(str))  # True

print('__len__' in dir(int))  # False
print('__len__' in dir(float))  # False

# 证明__len__这个方法在类list,dict,set,tuple,str中都存在，而在类int和float中是不存在的
# 而对象执行len() 时触发了此方法

# 自定义 __len__ 例子
class Class:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.students = []

    def __len__(self):
        return len(self.students)

s1 = Class('class 1', 'Big Data')
s1.students.append('laura')
s1.students.append('wendy')
s1.students.append('sinida')  # 改变对象属性
print(len(s1))  # 3  触发__len__方法