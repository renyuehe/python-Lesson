class animal:
    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

    def play(self):
        print("玩耍")

    def sleep(self):
        print("睡觉")

    def yelp(self):
        print("犬吠")


class Dog(animal):
    def yelp(self):
        print("特殊的犬吠")  # 和父类中方法名字相同，但是方法不一样，


pipi = Dog()

pipi.eat()
pipi.drink()
pipi.play()
pipi.yelp()
pipi.sleep






