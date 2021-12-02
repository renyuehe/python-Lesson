# 没有看出任何区别 服了
from typing import Optional

def fun1(start: int, end: int, ops: str = None) -> str:
    if ops:
        print("fun1 使用了可选参数")
    else:
        print("fun1 没有使用可选参数")
    return "str {0} end {1} fun1 可选参数 为{2}".format(start, end, ops)

def fun2(start: int, end: int, ops: Optional[str] = None) -> str:
    if ops:
        print("fun2 使用了可选参数")
    else:
        print("fun2 没有使用可选参数")
    return "str {0} end {1} fun2 可选参数 为{2}".format(start, end, ops)

# print(fun1(1,2,"哈哈"))
# print(fun2(2,10, "有锤子区别"))

fun1(1,2)
fun2(1,2,"a")