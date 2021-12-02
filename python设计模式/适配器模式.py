'''
适配器模式
意图

将一个类的接口转换成客户希望的另外一个接口。Adapter 模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
适用性：

你想使用一个已经存在的类，而它的接口不符合你的需求。

你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作
'''


# 适配器模式
# 将一个类的接口转换成客户希望的另外一个接口。使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
# 应用场景：希望复用一些现存的类，但是接口又与复用环境要求不一致。

def printInfo(info):
    print(info)


# 球员类
class Player():
    name = ''

    def __init__(self, name):
        self.name = name

    def Attack(self, name):
        pass

    def Defense(self):
        pass


# 前锋
class Forwards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("前锋%s 进攻" % self.name)

    def Defense(self, name):
        printInfo("前锋%s 防守" % self.name)


# 中锋（目标类）
class Center(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("中锋%s 进攻" % self.name)

    def Defense(self):
        printInfo("中锋%s 防守" % self.name)


# 后卫
class Guards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("后卫%s 进攻" % self.name)

    def Defense(self):
        printInfo("后卫%s 防守" % self.name)


# 外籍中锋（待适配类）
# 中锋
class ForeignCenter(Player):
    name = ''

    def __init__(self, name):
        Player.__init__(self, name)

    def ForeignAttack(self):
        printInfo("外籍中锋%s 进攻" % self.name)

    def ForeignDefense(self):
        printInfo("外籍中锋%s 防守" % self.name)


# 翻译（适配类）
class Translator(Player):
    foreignCenter = None

    def __init__(self, name):
        self.foreignCenter = ForeignCenter(name)

    def Attack(self):
        self.foreignCenter.ForeignAttack()

    def Defense(self):
        self.foreignCenter.ForeignDefense()


def clientUI():
    b = Forwards('巴蒂尔')
    m = Guards('姚明')
    ym = Translator('麦克格雷迪')

    b.Attack()
    m.Defense()
    ym.Attack()
    ym.Defense()
    return


if __name__ == '__main__':
    clientUI()