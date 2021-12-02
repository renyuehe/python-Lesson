
def myabc(funcobj):
    funcobj.__isabstractmethod__ = True
    print(funcobj.__isabstractmethod__)
    print(funcobj)

    return funcobj


class BBB():
    def __init__(self):
        pass
    @myabc
    def test(self):
        pass


b = BBB()
print(b)
print(BBB)
print(BBB.test)
print(BBB.test.__isabstractmethod__)
