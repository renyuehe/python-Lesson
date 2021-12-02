a = "hello"
b = "world"

# 字符串连接
c = a + " " + b
print(c)

print("=========================")

# 通过转义字符让字符串换行
d = a + "\n" + b
print(d)

print("=========================")
# 普通字符串和r字符串
print("hello\nworld")
print(r"hello\nworld")

print("=========================")
# 字符串切片操作
print(a[1:])

print("=========================")
# 查找字串llo
print(a.index("llo"))  # 如果不存在该字串会报错
print(a.find("llo"))  # 如果不存在该字串会返回-1

print("=========================")
# 格式化字符串
print("{} {}!".format(a, b))
print(f"{a} {b}!")
