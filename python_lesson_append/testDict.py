# 相当于 C++ 的 map

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"



print(dict['one'])  # 输出键为'one' 的值
print(dict[2])      # 输出键为 2 的值


tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
print(tinydict)     # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())    # 输出所有值

del tinydict['name']
print(tinydict)

tinydict.pop("code")
print(tinydict)

# 无，则增加
tinydict["age"] = 22
print(tinydict)
# 有，则修改
tinydict["age"] = 23
print(tinydict)

