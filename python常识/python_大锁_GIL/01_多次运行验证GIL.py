import threading
count = 0
def add():
  global count
  for i in range(10**6):
    count += 1

def minus():
  global count
  for i in range(10**6):
    count -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=minus)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(count)

'''
可以看到count并不是一个固定值，说明GIL会在某个时刻释放，那么GIL具体在什么情况下释放呢：
1.执行的字节码行数到达一定阈值
2.通过时间片划分，到达一定时间阈值
3.在遇到IO操作时，主动释放
'''