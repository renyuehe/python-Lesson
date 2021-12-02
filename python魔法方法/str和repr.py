class Test(object):
    def __init__(self, world):
        self.world = world

    def __str__(self):
        return 'world is %s str' % self.world

    def __repr__(self):
        return 'world is %s repr' % self.world

t = Test('world_big')
print(str(t))
print(repr(t))
print(t)