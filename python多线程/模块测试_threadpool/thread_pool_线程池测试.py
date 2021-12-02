import threadpool

# 调用sum函数求和
def sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

# 定义结果统一回调
totalsum = 0

def onresult(req, sum):
    global totalsum
    totalsum += sum

# 并发10条线程并求和
def threadpoolSum():
    # 创建需求列表
    reqlist = []
    for i in range(10):
        reqlist.append(([i * 10 ** 7 + 1, 10 ** 7 * (i + 1)], None))

    # 创建需求
    reqs = threadpool.makeRequests(sum, reqlist, callback=onresult)

    # 创建线程为10的线程池
    mypool = threadpool.ThreadPool(10)

    # 把需求添加到线程池
    for item in reqs:
        mypool.putRequest(item)

    # 阻塞等待
    mypool.wait()
    # 打印结果
    print(totalsum)

# 程序主入口
if __name__ == '__main__':
    threadpoolSum()