import os

'''
########################################################################
常用的系统环境变量
WINDOWS
os.environ['HOMEPATH']:当前用户主目录。
os.environ['TEMP']:临时目录路径。
os.environ["PATHEXT"]:可执行文件。
os.environ['SYSTEMROOT']:系统主目录。
os.environ['LOGONSERVER']:机器名。
os.environ['PROMPT']:设置提示符。

LINUX
os.environ['USER']:当前使用用户。
os.environ['LC_COLLATE']:路径扩展的结果排序时的字母顺序。
os.environ['SHELL']:使用shell的类型。
os.environ['LAN']:使用的语言。
os.environ['SSH_AUTH_SOCK']:ssh的执行路径。
'''

'''
########################################################################
# 设置系统环境变量
os.environ['环境变量名称']='环境变量值' #其中key和value均为string类型
os.putenv('环境变量名称', '环境变量值')
os.environ.setdefault('环境变量名称', '环境变量值')

# 修改系统环境变量
os.environ['环境变量名称']='新环境变量值'
# 获取系统环境变量
os.environ['环境变量名称']
os.getenv('环境变量名称')
os.environ.get('环境变量名称', '默认值')	#默认值可给可不给，环境变量不存在返回默认值

# 删除系统环境变量
del os.environ['环境变量名称']
del(os.environ['环境变量名称'])

# 判断当前系统是否存在环境变量
'环境变量值' in os.environ   # 存在返回 True，不存在返回 False
'''
print(os.environ["HOMEPATH"]) # 家目录
print(os.environ["TEMP"]) #临时文件目录
print(os.environ["PATHEXT"]) #可执行文件后缀
print(os.environ["SYSTEMROOT"]) #系统目录
print(os.environ["LOGONSERVER"]) #机器名
print(os.environ["PROMPT"]) #设置提示符？？
