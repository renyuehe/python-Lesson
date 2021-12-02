import os
print(os.path.abspath(os.path.curdir))
os.chdir(r"../")
print(os.path.abspath(os.path.curdir))