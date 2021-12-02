# 接下来我们来看下进程池：
import multiprocessing

# 调用sum函数求和
def sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

# 结果统一回调并处理
totalsum = 0

def onresult(sum):
    global totalsum
    totalsum += sum

def MultiprocessPoolSum():
    # 创建10条进程池
    mypool = multiprocessing.Pool(10)

    # 并发10条进程
    for i in range(10):
        mypool.apply_async(sum, (i * 10 ** 7 + 1, 10 ** 7 * (i + 1)), callback=onresult)
    # 关闭进程池
    mypool.close()
    # 阻塞等待
    mypool.join()
    print(totalsum)

# 程序主入口
if __name__ == '__main__':
    MultiprocessPoolSum()