import time

class AAA(object):
    def __init__(self, name):
        print("-----------------init------------------")
        self.name = name
        self.watch_tv_func = None
        self.have_dinner_func = None

    def get_up(self):
        print("-----------------get_up------------------")
        print("%s get up at:%s" % (self.name, time.time()))

    def go_to_sleep(self):
        print("-----------------go_to_sleep------------------")
        print("%s go to sleep at:%s" % (self.name, time.time()))

    def register_tv_hook(self, watch_tv_func):
        print("-----------------register_tv_hook------------------")
        self.watch_tv_func = watch_tv_func

    def register_dinner_hook(self, have_dinner_func):
        print("-----------------register_dinner_hook------------------")
        self.have_dinner_func = have_dinner_func

    def enjoy_a_lazy_day(self):
        print("-----------------enjoy_a_lazy_day------------------")

        # get up
        self.get_up()
        time.sleep(3)
        # watch tv
        # check the watch_tv_func(hooked or unhooked)
        # hooked
        if self.watch_tv_func is not None:
            self.watch_tv_func(self.name)
        # unhooked
        else:
            print("no tv to watch")
        time.sleep(3)
        # have dinner
        # check the have_dinner_func(hooked or unhooked)
        # hooked
        if self.have_dinner_func is not None:
            self.have_dinner_func(self.name)
        # unhooked
        else:
            print("nothing to eat at dinner")
        time.sleep(3)
        self.go_to_sleep()


def watch_daydayup(name):
    print("================watch_daydayup=================")
    print("%s : The program ---day day up--- is funny!!!" % name)


def watch_happyfamily(name):
    print("================watch_happyfamily=================")
    print("%s : The program ---happy family--- is boring!!!" % name)


def eat_meat(name):
    print("================eat_meat=================")
    print("%s : The meat is nice!!!" % name)


def eat_hamburger(name):
    print("%s : The hamburger is not so bad!!!" % name)


if __name__ == "__main__":
    aaa = AAA("Tom")
    aaa2 = AAA("Jerry")

    # register hook 注册钩子函数 ,钩子函数就是回调函数
    aaa.register_tv_hook(watch_daydayup)
    aaa.register_dinner_hook(eat_meat)

    aaa2.register_tv_hook(watch_happyfamily)
    aaa2.register_dinner_hook(eat_hamburger)

    # enjoy a day
    aaa.enjoy_a_lazy_day()
    # aaa2.enjoy_a_lazy_day()