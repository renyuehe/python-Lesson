
import os
def funa():
    print("funa")

if __name__ == '__main__':
    print(os.path.abspath(os.path.curdir)) #程序的执行路径是 B包
    from A import a

