####### 用法一 ： 父类调用子类方法  #######

class father():
    def call_children(self):
        child_method = getattr(self, 'out')# 获取子类的out()方法,采用反射的方式
        child_method() # 执行子类的out()方法

class children(father):
    def out(self):
        print("hehe")

child = children()
child.call_children()

##############