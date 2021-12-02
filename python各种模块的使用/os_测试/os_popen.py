import os

print(os.popen('mkdir new_folder').read()) # 创建成功的话没有任何返回值， 但是如果已经存在的话， 子目录或者文件 new_folder已经存在，
print(os.popen('ipconfig').read()) # 跟在cmd 窗口敲该命令结果一样， 显示该计算机的ip详情信息 不添加read的话，  <os._wrap_close object at 0x0000022554EBCFD0>