
import sys
print(sys.argv[0])
import os
sys.path.append(os.path.abspath(os.path.curdir))

print(sys.argv[0])
from python路径问题.subPackage import Net

if __name__ == '__main__':
    os.chdir(r"..")
    Net.NetFun()