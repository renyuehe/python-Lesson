from python常识.路径问题 import 获取当前代码路径
import os

print(获取当前代码路径.current_path)
print(获取当前代码路径.current_dir)

print(os.path.abspath(os.curdir))

获取当前代码路径.changeCurrentDir()
print(os.path.abspath(os.curdir))
