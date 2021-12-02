import os
print(os.system('cd ..')) # 结果会打印出来0， 表示命令执行成功， 否则表示执行失败，例如执行

print(os.system('mkdir new_folder'))  # 执行第一次， 结果是0 第二次返回值是子目录或者文件 new_folder已经存在，
# 目前来说，我在使用的时候没有出现太多的莫名其妙的错误，但是有大神说不建议用这个模块，由下面两种代替。
