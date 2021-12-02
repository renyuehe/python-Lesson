import os
print(os.path.abspath(os.path.curdir))
os.chdir(os.path.join("..", os.path.curdir))
print(os.path.abspath(os.path.curdir))