

def fun(a, b):
    return a,b #这样返回,默认包装成元组

def fun2(a, b):
    return (a,b)

def fun3(a, b):
    return [a,b]


print(fun(10,20))
print(fun2(10,20))
print(fun3(10,20))