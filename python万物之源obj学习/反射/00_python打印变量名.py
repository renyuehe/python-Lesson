
############## 通过 locals() 的方式
batch_size = 10
aa = 1
print(locals())

def getname(var):
    print(locals())
    return ([var_name for var_name, var_val in locals().items() if var_val is var])

print(getname(batch_size))

################### # 通过 gloabals() 的方式
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

ret = namestr(aa, globals())
print(ret)

################### 通过获取行信息的方式, 这也是动态语言的特点

import inspect
import re

def varname(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        print("----------->>"+line)
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)

print(varname(batch_size))


################ 还是相当于通过  inspect.currentframe().f_back.f_locals.items()

def retrieve_name(var):

    callers_local_vars = inspect.currentframe().f_back.f_locals.items()

    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

name, address, age, gender = "bob", "hangzhou", 21, "man"
person = {}

for i in [name, address, age, gender]:
    print(retrieve_name(i)[0])


