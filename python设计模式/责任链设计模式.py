'''
责任链模式 （场景:OA系统，项目审批...）
使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

适用性：

有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定。

代码示例：

流程审批，跟进需要审批的额度不同。需要的环节多少则不同
'''

class BaseHandler(object):
    _superior = None
    '''处理基类'''
    def submit_to_superior(self, superior):  # 向上级提交
        # 设置上级处理人
        self._superior = superior


class RequestHandlerL1(BaseHandler):
    '''第一级请求处理者'''
    name = "TeamLeader"

    def handle(self,request):
        if request < 500 :
            print("审批者[%s],请求金额[%s],审批结果[审批通过]"%(self.name,request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" %self.name)
            self._superior.handle(request)


class RequestHandlerL2(BaseHandler):
    '''第二级请求处理者'''
    name = "DeptManager"
    def handle(self,request):
        if request < 5000 :
            print("审批者[%s],请求金额[%s],审批结果[审批通过]"%(self.name,request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" %self.name)
            self._superior.handle(request)


class RequestHandlerL3(BaseHandler):
    '''第三级请求处理者'''
    name = "CEO"

    def handle(self,request):
        if request < 10000 :
            print("审批者[%s],请求金额[%s],审批结果[审批通过]"%(self.name,request))
        else:
            print("\033[31;1m[%s]要太多钱了,不批\033[0m"%self.name)


class RequestAPI(object):
    h1 = RequestHandlerL1()
    h2 = RequestHandlerL2()
    h3 = RequestHandlerL3()

    h1.submit_to_superior(h2)
    h2.submit_to_superior(h3)

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def handle(self):
        '''统一请求接口'''
        self.h1.handle(self.amount)


if __name__ == "__main__":
    r1 = RequestAPI("Alex", 50000)
    r1.handle()
    print(r1.__dict__)