import sys

ret = sys.path
import os

re2 = os.path.abspath(os.path.curdir)
print(ret)
print(re2)

print(__file__)
realpath = os.path.realpath(__file__)
print(realpath)

print("--------------")
print(sys.path)
sys.path.insert(0, "path")
print("------")
print(sys.path)