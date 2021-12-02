class AAA():
    def __init__(self):
        pass

    def disp_info(self):
        print("父类方法")

class BBB(AAA): #继承People
    def __init__(self):
        AAA.__init__(self)

    def disp_info(self): #方法重写
        print("子类方法")

bbb = BBB()

bbb.disp_info() #对象调用方法，调用的是重写后的方法
AAA.disp_info(bbb) #方法1：通过父类名+方法名的方式，调用父类的方法
super(BBB, bbb).disp_info() #方法2使用super

