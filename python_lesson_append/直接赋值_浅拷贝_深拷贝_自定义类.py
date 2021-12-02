'''
可以直接使用内置的copy,也可以通过copy.copy() copy.deepcopy()
两种方法效果一样
'''
import copy

class XY:
    def __init__(self):
        super(XY, self).__init__()
        self.ll = [1,2,3]


xy = XY()

print(xy.ll)
xx = copy.copy(xy)
print(xx)
print(xx.ll)
xy.ll.append(4)
print(xx.ll)