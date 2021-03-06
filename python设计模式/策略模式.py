'''
策略模式
意图：定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。

主要解决：在有多种算法相似的情况下，使用 if...else 所带来的复杂和难以维护。

何时使用：一个系统有许多许多类，而区分它们的只是他们直接的行为。

如何解决：将这些算法封装成一个一个的类，任意地替换。

关键代码：实现同一个接口。

应用实例： 1、诸葛亮的锦囊妙计，每一个锦囊就是一个策略。 2、旅行的出游方式，选择骑自行车、坐汽车，每一种旅行方式都是一个策略。 3、JAVA AWT 中的 LayoutManager。

优点： 1、算法可以自由切换。 2、避免使用多重条件判断。 3、扩展性良好。

缺点： 1、策略类会增多。 2、所有策略类都需要对外暴露。

使用场景： 1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。 2、一个系统需要动态地在几种算法中选择一种。 3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现。
'''

class TravelStrategy(object):
    '''
    出行策略
    '''

    def travelAlgorithm(self):
        pass


class AirplaneStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐飞机出行....")


class TrainStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐高铁出行....")


class CarStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("自驾出行....")


class BicycleStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("骑车出行....")


class TravelInterface(object):
    # 创建出行动作
    def __init__(self,travel_strategy):
        self.travel_strategy = travel_strategy

    # 更新出行方式
    def set_strategy(self,travel_strategy):
        self.travel_strategy = travel_strategy

    # 说走就走
    def travel(self):
        return self.travel_strategy.travelAlgorithm()



# 坐飞机
travel = TravelInterface(AirplaneStrategy())

travel.travel()

# 改开车
travel.set_strategy(CarStrategy())
travel.travel()