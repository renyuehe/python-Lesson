
class Base:
    def __init__(self, baseParm:str):
        self.baseParm = baseParm

class AAA(Base):
    def __init__(self, aaaParm):
        super(AAA, self).__init__(aaaParm)
        self.aaaParm = aaaParm

    def prt(self):
        print(self.baseParm)

a = AAA(aaaParm="你哈")

a.prt()