import os

# 用树形式遍历目录
for dirname, _, filenames in os.walk("../../"):
    print(dirname) # 目录名
    print(_) # 目录中的子目录
    print(filenames) # 目录中的文件夹
    print()